from django.shortcuts import render

#poniższa funkcja post_list pobiera i zwraca wartość uzyskaną dzięki wywołaniu innej funkcji wbudowanej w Django (render), która wyrenderuje (złoży w całość) szablon HTML.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

