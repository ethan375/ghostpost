from django.shortcuts import render
from .models import Post
from ghostpost.templates.forms.form import NewPost
from datetime import datetime


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)


def new_post(request):
    if request.method == 'POST':
        form = NewPost(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Post.objects.create(
                boast = data['boast'],
                post = data['post'],
                up_votes = 0,
                down_votes = 0,
            )
            return render(request, 'home.html')
        
    else:
        form = NewPost()
        context = {'form': form}
        return render(request, 'new_post.html', context)


def up_vote(request, id):
    post = Post.obejcts.filter(id=id)
    post.up_votes += 1
    post.save()


def down_vote(request, id):
    post = Post.obejcts.filter(id=id)
    post.down_votes += 1
    post.save()
