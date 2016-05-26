from models import Post
from django.utils import timezone
from django.shortcuts import render
from forms import PostForm, UserForm
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response


# blog views

def post_list(request):
    # posts = Post.objects.all()
    posts=Post.objects.filter(author=request.user)
    return render(request, 'headland/blog/post_list.html', { 'posts':posts })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'headland/blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'headland/blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'headland/blog/post_edit.html', {'form': form})


# about views

def contact(request):
    return render(request, 'headland/contact.html')


@login_required
def home(request):
    return render(request, 'headland/home.html')