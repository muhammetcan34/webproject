from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import postt
from .forms import PostForm
from django.contrib import messages



def post_index(request):
    posts = postt.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(postt, id=id)
    context = {
        'post': post,

    }

    return render(request, 'post/detail.html', context)


def post_create(request):


   # if request.method == "POST":
    #    print(request.POST)

  #  title = request.POST.get('title')
   # content = request.POST.get('content')
    #postt = objects.create(title=title, content=content)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
           postttt = form.save()
        messages.success(request, ' başarıyla olusturdunuz. ')

        return HttpResponseRedirect("/post/{}/detail".format(postttt.id))

    else:
        form = PostForm()
    form = PostForm()
    context = {
        'form': form,
    }


    return render(request, 'post/form.html', context)


def post_update(request, id):
    post = get_object_or_404(postt, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        posttt = form.save()
        messages.success(request, 'postunuz başarıyla güncellendi')

        return HttpResponseRedirect("/post/{}/detail".format(posttt.id))

    context = {
        'form': form,
    }


    return render(request, 'post/form.html', context)

def post_delete(request, id):
    post = get_object_or_404(postt, id=id)
    post.delete()
    messages.success(request,  f"postunuz başarıyla silindi ")
    return redirect('post:index')

    return HttpResponse('burasi post delete sayfasi')

