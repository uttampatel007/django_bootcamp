from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from blog.forms import PostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def homepage(request):
    """Homepage view"""
    return render(request, 'blog/homepage.html')

@login_required
def blog(request):
    """blog listing view"""

    blogs = Post.objects.all()

    context = {
        'all_blog':blogs,
        'project_name': "This is Google.com"
    }
    return render(request, 'blog/blog_list.html', context)

@login_required
def blog_post(request, id):
    
    # blog_post = [blog for blog in blogs if blog['slug'] == slug]
    try:
        blog_post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return render(request, 'blog/404.html')

    context = {
        'blog_post': blog_post
    }

    return render(request, 'blog/blog_post.html', context)


def example_route(request):
    context = {
        "project_name": "This is Youtube.com",
        "greetings": "Hello World!!!",
        "fruit_list": ["Apple", "Banana", "Mango", "Orange", "Papaya"],
        "is_user_logged_in": True
    }
    return render(request, 'blog/example_route.html', context)


def authors(request):
    return render(request, 'blog/authors.html')


def blog_post_create(request):
    
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
        
            return redirect('blog:blog_list')
        else:
            # form.errors()
            return HttpResponse('Invalid form')

    form = PostModelForm()
    context = {
        'form': form
    }
    return render(request, 'blog/blog_create.html', context)


def blog_post_update(request, id):
    instance = Post.objects.get(id=id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()

            return redirect('blog:blog_post', id=id)
        else:
            # form.errors()
            return HttpResponse('Invalid form')

    form = PostModelForm(instance=instance)

    context = {
        "form":form
    }
    return render(request, 'blog/blog_update.html', context)


def signup(request):
    """Signup view"""

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    form = UserCreationForm()
    context = {
        "form":form
    }
    return render(request, 'blog/signup.html', context)


# -> url -> view -> data from db -> using context send data to template -> render that data