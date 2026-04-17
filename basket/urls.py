from django.urls import path
from basket.views import create_order_view, read_order_view, update_order_view, delete_order_view

app_name='basket'

urlpatterns = [
    path('create_order/', create_order_view, name='add_order'),
    path('order_list/', read_order_view, name='orders'),
    path('order_list/<int:id>/update/', update_order_view),
    path('order_list/<int:id>/delete/', delete_order_view),

]