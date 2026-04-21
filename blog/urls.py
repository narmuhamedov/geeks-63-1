from django.urls import path
from . import views

urlpatterns = [
    path('fist_message/', views.FirstMessageView.as_view()),
    path('second_message/', views.second_message_view),
    path('photo_message/', views.photo_message_view),
    path('blog_list/', views.BlogListView.as_view()),
    path('blog_list/<int:id>/', views.BookDetailView.as_view()),
    path('search/',views.SearchView.as_view()),
]