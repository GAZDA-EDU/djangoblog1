from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import PostForm
from django.views.generic import DeleteView
from django.views.generic import TemplateView


class Image(TemplateView):
    form = PostForm
    template_name = 'blog/image.html'

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('image_display', kwargs={'pk': obj.id}))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ImageDisplay(DeleteView):
    model = Post
    template_name = 'blog/image_display.html'
    context_object_name = 'image'


# poniższa funkcja post_list pobiera i zwraca wartość uzyskaną dzięki wywołaniu innej funkcji wbudowanej w Django (render), która wyrenderuje (złoży w całość) szablon HTML.

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def error_404_view(request, exception):
    data = {"name": 'Blog dla programistów'}
    return render(request, 'blog/404.html', data)


#def error_500_view(request, exception):
#    data = {"name": 'Blog dla programistów'}
#    return render(request, 'blog/500.html', data)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
