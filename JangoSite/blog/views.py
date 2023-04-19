from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(status=Post.PostStatus.PUBLISHED)
    return render(request, 'blog/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/detail.html', {'post': post})
