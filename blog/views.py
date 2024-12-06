from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from blog.forms import BlogForm, PostForm, ReactionForm
from blog.models import Blog, Post, Reaction
from blog.services.blog_service import BlogService
from blog.services.comment_service import CommentService
from blog.services.post_service import PostService
from users.forms import CommentForm
from users.models import Comment, TextComments

blog_service = BlogService()

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        title = request.POST['title']
        if form.is_valid():
            blog_service.add_blog(title)
            return redirect('main:index')
    else:
        form = BlogForm()

    return render(request, 'blog/creation.html', {'form': form})

def get_blog(request, blog_id):
    blog = blog_service.get_blog(blog_id)
    posts = blog.posts.all()
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, id=post_id)
            text_comment = TextComments.objects.create(text=comment_form.cleaned_data['text'])
            Comment.objects.create(user=request.user, text=text_comment, post=post)
            return redirect('blog:get_blog', blog_id=blog.id)

    return render(request, 'blog/blog_content.html', {
        'blog': blog,
        'posts': posts,
        'comment_form': comment_form,
    })

def set_blog_name(request, blog_id):
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        if not new_name:
            return HttpResponseBadRequest("Не указано новое название блога.")
        blog_service.set_blog_name(blog_id, new_name)
        return redirect('blog:get_blog', blog_id=blog_id)
    return HttpResponseBadRequest("Метод запроса должен быть POST.")

def delete_blog(request, blog_id):
    if request.method == 'POST':
        if blog_service.delete_blog(blog_id):
            return JsonResponse({'message': 'Блог успешно удалён.'})
        return HttpResponseNotFound("Блог с указанным идентификатором не найден.")
    return HttpResponseBadRequest("Метод запроса должен быть POST.")

def get_blog_name(request, blog_id):
    blog_name = blog_service.get_blog_name(blog_id)
    return JsonResponse({'blog_name': blog_name})
    

post_service = PostService()

def add_post(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_service.add_post(user=request.user, blog=blog, text=form.cleaned_data['text'], image=form.cleaned_data['image'])
            return redirect('blog:get_blog', blog_id=blog.id)
    else:
        form = PostForm()

    return render(request, 'blog/creation_post.html', {'form': form, 'blog': blog})

def delete_post(request, post_id):
    if request.method == 'POST':
        post_service.delete_post(post_id)
        return redirect('main:index')

def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_service.update_post(post_id, text=form.cleaned_data['text'], image=form.cleaned_data['image'])
            return redirect('blog:get_blog', blog_id=post.blog.id)
    else:
        form = PostForm(initial={'text': post.post_body.text, 'image': post.post_body.image})

    return render(request, 'blog/creation_post.html', {'form': form, 'blog': post.blog})

def get_post(request, post_id):
    post = post_service.get_post(post_id) 
    return render(request, 'blog/blog_content.html', {'post': post})

comment_service = CommentService()

def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_service.add_comment(user=request.user, post_id=post_id, text=form.cleaned_data['text'])
            return redirect('blog:blog_content', blog_id=request.POST['blog_id'])  

    return redirect('blog:blog_content', blog_id=post_id)  

def delete_comment(request, comment_id):
    if request.method == 'POST':
        comment_service.delete_comment(comment_id)
        return redirect('main:index') 
    
def get_comments(request, post_id):
    comments = comment_service.get_comments(post_id)
    return render(request, 'blog/comments.html', {'comments': comments})

def react_to_post(request):
    if request.method == 'POST':
        form = ReactionForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, id=form.cleaned_data['post_id'])
            reaction_type = form.cleaned_data['reaction_type']

            reaction, created = Reaction.objects.get_or_create(user=request.user, post=post)
            if reaction.reaction_type == reaction_type:
                reaction.delete() 
            else:
                reaction.reaction_type = reaction_type
                reaction.save()
            
            return render(
                request,
                'blog/blog_content.html',
                {
                    'blog': post.blog,
                    'posts': post.blog.posts.all(), 
                    'comment_form': CommentForm(),  
                },
            )
    else:
        return render(request, 'blog/blog_content.html')