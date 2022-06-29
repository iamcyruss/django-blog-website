from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import BlogPost
from .forms import FormIngest


def index(request):
    return render(request, 'index.html')


def blog_list(request):
    blogs = BlogPost.objects.all()
    blogs = reversed(blogs)
    return render(request, 'blogs.html', context={'blogs': blogs})


def blog_detail(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    return render(request, 'blog.html', context={'blog': blog})


def about_me(request):
    me = BlogPost.objects.all()
    me = reversed(me)
    return render(request, 'aboutme.html', context={'me': me})


def form_ingest(request):
    #submitted = False
    if request.method == "POST":
        title = request.POST['title']
        summary = request.POST['summary']
        learned = request.POST['learned']
        img_url = request.POST['img_url']
        git_url = request.POST['git_url']
        new_blog_post = BlogPost(title=title, summary=summary, learned=learned, img_url=img_url, git_url=git_url)
        new_blog_post.save()
        """
        if new_blog_post.is_valid():
            new_blog_post.save()
            return HttpResponseRedirect('/form_ingest?submitted=True')
        else:
            form = FormIngest
            if 'submitted' in request.Get:
                submitted = True
                """

    return render(request, 'blogpost.html', {})
