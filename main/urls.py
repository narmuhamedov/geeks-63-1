"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from blog.views import fist_message_view, second_message_view, photo_message_view, blog_list_view, blog_detail_view
from connection_database.views import car_list_view

from basket.views import create_order_view, read_order_view, update_order_view, delete_order_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fist_message/', fist_message_view),
    path('second_message/', second_message_view),
    path('photo_message/', photo_message_view),
    path('blog_list/', blog_list_view),
    path('blog_list/<int:id>/', blog_detail_view),
    path('car_list/', car_list_view),
    
    path('create_order/', create_order_view),
    path('order_list/', read_order_view),
    path('order_list/<int:id>/update/', update_order_view),
    path('order_list/<int:id>/delete/', delete_order_view),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
