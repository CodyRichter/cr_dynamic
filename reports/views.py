import datetime

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from reports.forms import PostForm
from reports.models import Post


@login_required(login_url='/auth/login')
def index(request):
    cdt = datetime.datetime.now()
    post_today = Post.objects.all().filter(release_date__date=datetime.date.today()).order_by('release_date')
    post_past = Post.objects.all().filter(release_date__lt=datetime.date.today()).order_by('release_date')
    my_post = Post.objects.all().filter(author=request.user).order_by('release_date')
    context = {'post_today': post_today,
               'post_past': post_past,
               'my_post': my_post,
               'cdt': cdt}
    return render(request, 'reports/index.html', context)


@login_required(login_url='/auth/login')
def new(request):
    if request.method == 'POST':
        formset = PostForm(request.POST, request.FILES)
        formset.instance.author = request.user
        if formset.is_valid():
            formset.save()
            return redirect('/reports/' + str(formset.instance.id))
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
            return redirect('/reports/' + str(post_id))
    else:
        form = PostForm(instance=post)
    return render(request, 'reports/edit.html', {'form': form})


@login_required(login_url='/auth/login')
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.author != request.user:
        messages.error(request, 'You do not have permission to delete this post.')
        return redirect('/reports/')
    post.delete()
    messages.success(request, 'Post successfully deleted.')
    return redirect('/reports/')


@login_required(login_url='/auth/login')
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.release_date.date() > datetime.datetime.today().date() and post.author != request.user:
        messages.error(request, 'You do not have permission to view this post.')
        return redirect('/reports/')
    return render(request, 'reports/detail.html', {'post': post})
