from django.shortcuts import render, redirect, get_object_or_404
from basket.forms import BasketForm
from basket.models import Basket
from django.views import generic
from django.urls import reverse


#CREATE ORDER
class CreateOrderView(generic.CreateView):
    template_name = 'create_order.html'
    form_class = BasketForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateOrderView, self).form_valid(form=form)
    
    def get_success_url(self):
        return reverse('basket:orders')






# def create_order_view(request):
#     if request.method == "POST":
#         form = BasketForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('basket:orders')
#     else:
#         form = BasketForm()
#     return render(
#         request,
#         'create_order.html',
#         {
#             "form":form
#         }
#     )

#Read
class ReadOrderView(generic.ListView):
    template_name = 'order_list.html'
    model = Basket
    context_object_name = 'basket_list'

    def get_queryset(self):
        return self.model.objects.all()


# def read_order_view(request):
#     if request.method == "GET":
#         basket_list =  Basket.objects.all().order_by("-id")
#         return render(
#             request,
#             'order_list.html',
#             {
#                 "basket_list": basket_list
#             }
#         )


class UpdateOrderView(generic.UpdateView):
    template_name = 'update_order.html'
    form_class = BasketForm
    model = Basket
    success_url = '/order_list/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=order_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateOrderView, self).form_valid(form=form)








# def update_order_view(request, id):
#     order_id = get_object_or_404(Basket, id=id)
#     if request.method == "POST":
#         form = BasketForm(request.POST, instance=order_id)
#         if form.is_valid():
#             form.save()
#             return redirect('/order_list/')
#     else:
#         form = BasketForm(instance=order_id)
#     return render(
#         request,
#         'update_order.html',
#         {
#             "form": form,
#             "order_id": order_id
#         }
#     )




class DeleteOrderView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    model = Basket
    context_object_name = 'order_id'
    success_url = '/order_list/'



    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=order_id)


# def delete_order_view(request, id):
#     order_id = get_object_or_404(Basket, id=id)
#     order_id.delete()
#     return redirect('/order_list/')