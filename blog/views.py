from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'blog/index.html', locals())

def detail(request, blog_id):
    # return render(request, 'blog/detail.html', {'blog_id': blog_id})
    return render(request, 'blog/detail.html', locals())