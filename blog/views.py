from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

#poniższa funkcja post_list pobiera i zwraca wartość uzyskaną dzięki wywołaniu innej funkcji wbudowanej w Django (render), która wyrenderuje (złoży w całość) szablon HTML.

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

