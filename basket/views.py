from django.shortcuts import render, redirect, get_object_or_404
from basket.forms import BasketForm
from basket.models import Basket




#CREATE ORDER
def create_order_view(request):
    if request.method == "POST":
        form = BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basket:orders')
    else:
        form = BasketForm()
    return render(
        request,
        'create_order.html',
        {
            "form":form
        }
    )

#Read
def read_order_view(request):
    if request.method == "GET":
        basket_list =  Basket.objects.all().order_by("-id")
        return render(
            request,
            'order_list.html',
            {
                "basket_list": basket_list
            }
        )

def update_order_view(request, id):
    order_id = get_object_or_404(Basket, id=id)
    if request.method == "POST":
        form = BasketForm(request.POST, instance=order_id)
        if form.is_valid():
            form.save()
            return redirect('/order_list/')
    else:
        form = BasketForm(instance=order_id)
    return render(
        request,
        'update_order.html',
        {
            "form": form,
            "order_id": order_id
        }
    )


def delete_order_view(request, id):
    order_id = get_object_or_404(Basket, id=id)
    order_id.delete()
    return redirect('/order_list/')