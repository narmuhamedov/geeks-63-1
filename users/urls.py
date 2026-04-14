from django.urls import path
from users.views import register_view, auth_login_view, auth_logout_view, user_list_view

urlpatterns = [
    path('register/', register_view),
    path('login/', auth_login_view),
    path('logout/', auth_logout_view),
    path('user_list/', user_list_view)
]