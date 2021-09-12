from core.models import Condtion
from order.models import Order
from car.models import Car
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from .forms import OrderForm


class OrderPageView(TemplateView):
    template_name = 'userinfo.html'


def detail(request,pk):
    car = Car.objects.get(pk=pk)
    form = OrderForm()
    condition = Condtion.objects.first()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print(form.errors)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.car = car
            obj.save()
            return redirect('/')
    context = {
        'car':car,
        'form':form,
        'condition':condition,
    }
    return render(request,'userinfo.html',context)

