from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog
from django.core.paginator import Paginator
from django.db.models import F


def search_view(request):
    query = request.GET.get('s', '')
    if query:
        blog = Blog.objects.filter(title__icontains=query)
    else:
        return HttpResponse('Блог не найден')

    return render(
        request,
        'blog_list.html',
        {'blog': blog}
    )





def blog_detail_view(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(Blog, id=id)
        views_blog = request.session.get("viewed_blog", [])
        
        if id not in views_blog:
            blog_id.views = F("views")+1
            blog_id.save()
            blog_id.refresh_from_db()
        
        views_blog.append(id)
        request.session['viewed_blog'] = views_blog


        

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
        paginator = Paginator(blog, 2)
        page = request.GET.get("page")
        page_obj = paginator.get_page(page)

        return render(
            request,
            "blog_list.html",
            {
                "blog": page_obj,
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