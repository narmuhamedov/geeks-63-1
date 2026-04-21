from django.urls import path
#from basket.views import create_order_view, read_order_view, update_order_view, delete_order_view
from . import views
app_name='basket'

urlpatterns = [
    path('create_order/', views.CreateOrderView.as_view(), name='add_order'),
    path('order_list/', views.ReadOrderView.as_view(), name='orders'),
    path('order_list/<int:id>/update/', views.UpdateOrderView.as_view()),
    path('order_list/<int:id>/delete/', views.DeleteOrderView.as_view()),

]