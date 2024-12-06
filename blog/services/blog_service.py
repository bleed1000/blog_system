from ..models import Blog

class BlogService:
    def get_blog(self, blog_id):
        return Blog.objects.get(id=blog_id)
    
    def get_blog_name(self, blog_id):
        blog = Blog.objects.get(id=blog_id)
        return blog.title

    def set_blog_name(self, blog_id, new_name):
        blog = Blog.objects.get(id=blog_id)
        blog.title = new_name
        blog.save()
        return True

    def add_blog(self, blog_title):
        blog = Blog(title=blog_title)
        blog.save()
        return None

    def delete_blog(self, blog_id):
        if Blog.objects.filter(id=blog_id).exists():
            Blog.objects.filter(id=blog_id).delete()
            return True

