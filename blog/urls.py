from django.urls import path
from blog.views import fist_message_view, search_view, second_message_view, photo_message_view, blog_list_view, blog_detail_view


urlpatterns = [
    path('fist_message/', fist_message_view),
    path('second_message/', second_message_view),
    path('photo_message/', photo_message_view),
    path('blog_list/', blog_list_view),
    path('blog_list/<int:id>/', blog_detail_view),
    path('search/',search_view),
]