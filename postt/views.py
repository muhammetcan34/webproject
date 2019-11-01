from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import postt
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def post_index(request):
    post_list = postt.objects.all().order_by("-publishing_date")
    query = request.GET.get('q')
    if query:
        post_list =post_list.filter(
                            Q(title__icontains=query) |
                            Q(content__icontains=query) |
                            Q(user__first_name__icontains=query) |
                            Q(user__last_name__icontains=query)
                            ).distinct()



        paginator = Paginator(post_list, 5)  # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)

       

    return render(request, 'post/index.html', {'posts': post_list})

def post_detail(request, id):
    post = get_object_or_404(postt, id=id)
    context = {
        'post': post,

    }

    return render(request, 'post/detail.html', context)


def post_create(request):
    if not request.user.is_authenticated:
        return Http404()


    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
           postttt = form.save(commit=False)
           postttt.user = request.user
           postttt.save()
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
    form = PostForm(request.POST or None,  request.FILES or None, instance=post)
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

