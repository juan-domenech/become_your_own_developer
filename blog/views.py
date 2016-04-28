from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from .models import Post
from .forms import BlogPostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now() ).order_by('-published_date')
    return render(request, "blogposts.html",{'posts' : posts } )


def post_detail(request,id):
    post = get_object_or_404(Post,pk=id)
    # clock up the number of post views
    post.views += 1
    post.save()
    return render(request, "blogdetail.html",{'post' : post} )


@login_required(login_url='/login/')
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Let's make sure only the author can edit
    if post.author != auth.get_user(request):
        return render(request, 'edit_post_alert.html')
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form} )