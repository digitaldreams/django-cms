from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post, Category, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def category_index(request):
    categories = get_list_or_404(Category)
    return render(request, 'blog/categories/index.html', {'categories': categories})



def post_index(request):
    posts = get_list_or_404(Post)
    return render(request, 'blog/posts/index.html', {'posts': posts})


def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/posts/show.html', {'post': post})


def comment_save(request, post_id):
    try:
        post = get_object_or_404(Post, pk=post_id)
        comment = Comment(post_id=post.id, body=request.POST['body'], user=0)
        comment.save()
    except Exception as e:
        return HttpResponse(str(e))
    else:
        return HttpResponseRedirect(reverse('blog:posts.show', args=(post_id,)))
