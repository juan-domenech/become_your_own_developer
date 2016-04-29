from django.shortcuts import render
from django.utils import timezone
from blog.models import Post


def home(request):
    # In Home we paint all the available objects in the database (Post, Subjects, etc.)

    # Get all the active Posts
    posts = Post.objects.filter(published_date__lte = timezone.now() ).order_by('-published_date')


    return render(request, "home.html",{'posts' : posts } )