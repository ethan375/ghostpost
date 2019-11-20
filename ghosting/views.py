from django.shortcuts import render
from .models import Post
from ghostpost.templates.forms.form import NewPost
from datetime import datetime


def home(request):
    return render(request, 'home.html')


def new_post(request):
    if request.method == 'POST':
        form = NewPost(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            post = Post.objects.create(
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
