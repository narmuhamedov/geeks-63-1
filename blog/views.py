from django.shortcuts import render
from django.http import HttpResponse

def fist_message_view(request):
    if request.method == "GET":
        return HttpResponse('Hello World')


def second_message_view(request):
    if request.method == "GET":
        return HttpResponse('😀😄😁😆')

def photo_message_view(request):
    if request.method == "GET":
        return HttpResponse("<img src='https://avatarko.ru/img/kartinka/1/multfilm_pingviny.jpg'> <p>Пингвины</p>")