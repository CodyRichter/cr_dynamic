import datetime

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from reports.forms import PostForm
from reports.models import Post


@login_required(login_url='/auth/login')
def index(request):
    latest_post_list = Post.objects.all()
    context = {'latest_post_list': latest_post_list}
    return render(request, 'reports/index.html', context)


@login_required(login_url='/auth/login')
def new(request):
    if request.method == 'POST':
        formset = PostForm(request.POST, request.FILES)
        formset.instance.author = request.user.id
        formset.instance.seen = False
        formset.instance.pub_date = datetime.datetime.now()
        if formset.is_valid():
            formset.save()
            return redirect('/reports/'+str(formset.instance.id))
    else:
        formset = PostForm()
    return render(request, 'reports/new.html', {'formset': formset})


@login_required(login_url='/auth/login')
def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        messages.error(request, 'You do not have permission to edit this post.')
        return redirect('/reports/' + str(post_id))
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/reports/'+str(post_id))
    else:
        form = PostForm(instance=post)
    return render(request, 'reports/edit.html', {'form': form})


@login_required(login_url='/auth/login')
def delete(request, post_id):

    post = Post.objects.get(id=post_id)
    post.delete()
    return render(request, 'reports/index.html')


@login_required(login_url='/auth/login')
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if not post.seen:
        post.seen = True
        post.save()
    return render(request, 'reports/detail.html', {'post': post})