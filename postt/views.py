from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import postt
from .forms import PostForm


def post_index(request):
    posts = postt.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(postt, id=id)
    context = {
        'post':post,

    }

    return render(request, 'post/detail.html', context)


def post_create(request):

    form = PostForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        print(request.POST)

    return render(request, 'post/form.html', context)


def post_update(request):

    return HttpResponse('burasi post update sayfasi')

def post_delete(request):

    return HttpResponse('burasi post delete sayfasi')
