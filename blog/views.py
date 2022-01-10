from django.shortcuts import render,get_object_or_404
from .models import BlogProject
# Create your views here.
def all_blogs(request):
    blogs = BlogProject.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request,blog_id):

    blogs = get_object_or_404(BlogProject,pk = blog_id)
    return render(request,'blog/detail.html',{'blog':blogs})