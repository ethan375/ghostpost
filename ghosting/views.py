from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Post
from ghostpost.templates.forms.form import NewPost
from datetime import datetime


def home(request):
    posts = Post.objects.order_by('-creation_time')
    context = {'posts': posts}
    return render(request, 'home.html', context)


def boasts(request):
    posts = Post.objects.filter(boast=True)
    context = {'posts': posts}
    return render(request, 'home.html', context)


def roasts(request):
    posts = Post.objects.filter(boast=False)
    context = {'posts': posts}
    return render(request, 'home.html', context)


def votes(request):
    posts = sorted(Post.objects.all(), key=lambda p: p.total_votes)
    posts = posts[::-1]
    context = {'posts': posts}
    return render(request, 'home.html', context)


def new_post(request):
    if request.method == 'POST':
        form = NewPost(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Post.objects.create(
                boast = data['boast'],
                post = data['post']
            )
            return redirect('/ghosting/')
        
    else:
        form = NewPost()
        context = {'form': form}
        return render(request, 'new_post.html', context)


def up_vote(request, id):
    post = Post.objects.filter(id=id).first()
    post.up_votes += 1
    post.save()
    return redirect('/ghosting/')


def down_vote(request, id):
    post = Post.objects.filter(id=id).first()
    post.down_votes += 1
    post.save()
    return redirect('/ghosting/')
