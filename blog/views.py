from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post, Category, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.views.decorators.http import require_GET, require_http_methods, require_POST


@require_GET
def category_index(request):
    categories = get_list_or_404(Category)
    return render(request, 'blog/categories/index.html', {'categories': categories})


@require_GET
def post_index(request):
    # posts = get_list_or_404(Post)
    # Only show posts which are published
    posts = Post.objects.filter(status='published')
    return render(request, 'blog/posts/index.html', {'posts': posts})


@require_GET
def post_show(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/posts/show.html', {'post': post})


@require_POST
def comment_save(request, post_id):
    try:
        post = get_object_or_404(Post, pk=post_id)
        comment = Comment(post_id=post.id, body=request.POST['body'], user=0)
        comment.clean()
        comment.save()
    except ValidationError as e:
        return HttpResponse(str(e))
    else:
        return HttpResponseRedirect(reverse('blog:posts.show', args=(post_id,)))
