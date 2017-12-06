from django.shortcuts import render


def post_index(request):
    return render(request, 'blog/posts/index.html', {})
