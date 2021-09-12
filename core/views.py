from order.models import Order
from django.db.models.query import QuerySet
from order.forms import OrderForm
from core.forms import ContactForm
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from car.models import Catagory, Car
from .models import About, Condtion, Quote
from django.contrib import messages





class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car_cat"] = Catagory.objects.all()
        context["about"] = About.objects.first()
        context['form'] = ContactForm()
        context['quotes'] = Quote.objects.all()
        context['cars'] = Car.objects.all()[:6]
        return context


class ConditionPageView(TemplateView):

    template_name = 'conditions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["condition"] = Condtion.objects.first()
        return context
    

class CarPageView(TemplateView):

    template_name = 'all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = Car.objects.all()
        return context

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,'Mesaj Göndərildi')
        return redirect('/#contact')