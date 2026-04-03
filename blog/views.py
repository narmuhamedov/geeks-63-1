from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog


def blog_detail_view(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(Blog, id=id)
        return render(
            request,
            'blog_detail.html',
            {
                "blog_id": blog_id
            }
        )




def blog_list_view(request):
    if request.method == "GET":
        blog = Blog.objects.all().order_by("-id")
        return render(
            request,
            "blog_list.html",
            {
                "blog": blog
            }
        )













def fist_message_view(request):
    if request.method == "GET":
        return HttpResponse('Hello World')


def second_message_view(request):
    if request.method == "GET":
        return HttpResponse('😀😄😁😆')

def photo_message_view(request):
    if request.method == "GET":
        return HttpResponse("<img src='https://avatarko.ru/img/kartinka/1/multfilm_pingviny.jpg'> <p>Пингвины</p>")