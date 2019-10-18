from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import postt


def post_index(request):
    posts = postt.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def post_detail(request):
    post = get_object_or_404(postt, id=1)
    context = {
        'post':post,

    }

    return render(request, 'post/index.html',context)


def post_create(request):

    return HttpResponse('burasi post create sayfasi')


def post_update(request):

    return HttpResponse('burasi post update sayfasi')

def post_delete(request):

    return HttpResponse('burasi post delete sayfasi')
