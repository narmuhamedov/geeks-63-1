from django.urls import path
# from users.views import register_view, auth_login_view, auth_logout_view, user_list_view

from . import views
urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.AuthLoginView.as_view()),
    path('logout/', views.AuthLogoutView.as_view()),
    path('user_list/', views.user_list_view, name='user_list'),
]