from django.shortcuts import render

# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def render_index(request):
    my_list = {
        "app": "Django"
    }
    return render(request, 'index.html', my_list)
