from models import Post
from models import UserProfile
from django.utils import timezone
from django.shortcuts import render
from django.template import RequestContext
from forms import PostForm, UserProfileForm
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from awesome_avatar import forms as avatar_forms
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response


class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "headland/user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "headland/edit_profile.html"

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("profile", kwargs={'slug': self.request.user})


def change_avatar(request):
    if request.method == 'POST':
        form = AvatarChangeForm(request.POST, request.FILES,
                                instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/')
    else:
        form = AvatarChangeForm(instance=request.user.profile)

    return render(request, 'headland/edit_profile.html', {'form': form})


def upload_and_crop_image(request):
    if request.method == 'POST':
        form = UploadAndCropImageForm(request.POST)

        if form.is_valid():
            Images(image=form.image).save()
            return HttpResponseRedirect('/news/')
    else:
        form = UploadAndCropImageForm()

    return render(request, 'headland/edit_profile.html', {'form': form})



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