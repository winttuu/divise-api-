# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views.generic import CreateView,DeleteView,UpdateView,ListView
# from .forms import CurrencyForm
# from .models import Currency


# class CurrencyList(ListView):
#     model = Currency
#     template_name = 'index.html'


# class CurrencyCreate(CreateView):
#     model = Currency
#     form_class = CurrencyForm
#     template_name = 'create_currency.html'
#     succes_url = reverse_lazy('index')

# class CurrencyUpdate(UpdateView):
#     model = Currency
#     form_class = CurrencyForm
#     template_name = 'create_currency.html'
#     succes_url = reverse_lazy('index')

# class CurrencyDelete(DeleteView):
#     model = Currency
#     template_name = 'verification.html'
#     succes_url = reverse_lazy('index')

