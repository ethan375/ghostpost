from django.shortcuts import render
from ghostpost.templates.forms.form import NewPost


def home(request):
    return render(request, 'home.html')


def new_post(request):
    if request.method == 'POST':
        pass
    else:
        form = NewPost()
        context = {'form': form}
        return render(request, 'new_post.html', context)
