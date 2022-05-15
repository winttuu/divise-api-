import json
from locale import currency
from multiprocessing.dummy import current_process
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from api.models import Currency

class Divise(View):
    def get(self, request, **kwargs):
        try:
            id = kwargs.get('id')
            currency = Currency.objects.get(pk=id).to_json()
            return JsonResponse ({
                'response': currency,
                'status': 200
            })
        except:
            return JsonResponse ({
                'response': {},
                'status': 500
            })

    def post(self, request):
        try:
            data = json.loads(request.body)
            currency = self._create_current(data['usd_price'], data['divise'])
            print(data)

            return JsonResponse({
                'response': currency.to_json()
            })
        except:
            return JsonResponse({
                'response': {},
                'status': 500
            })

    def _create_current(self, usd_price, divise):
        currency = Currency()
        currency.usd_price = usd_price
        currency.divise = divise
        currency.save()

        return currency

    
    def put(self, request, **kwargs):
        try: 
            id = kwargs.get('id')
            currency = Currency.objects.get(pk=id).to_json()

            data = json.loads(request.body)
            currency = self._update_currency(data['usd_price'], data['divise'])

            return JsonResponse({
                'response': currency.to_json()
            })
        except:
            return JsonResponse({
                'response': {},
                'status': 500
            })

    def _update_currency(self, usd_price, divise):
        currency = Currency()
        currency.usd_price = usd_price
        currency.divise = divise
        currency.save()

        return currency

    
    def delete(self, request, **kwargs):
        try: 
            id = kwargs.get('id')
            Currency.objects.filter(id=id).delete()

            return JsonResponse({
                'message': 'eliminado exitosamente'
            })
        except:
            return JsonResponse({
                'response': {},
                'status': 500
            })

divise = Divise.as_view()































        
# from locale import currency
# from django.shortcuts import redirect, render
# # from .models import Currency
# # from .forms import CurrencyForm

# def inicio(request):   
#     currencys = Currency.objects.all()    #select * from Currency
#     contexto = {
#         'currencys':currencys
#     }
#     return render(request, 'index.html',contexto)


# def createCurrency(request):
#     if request.method == 'GET':
#         form = CurrencyForm()
#         contexto = {
#             'form':form
#         }
#     else:
#         form = CurrencyForm(request.POST)
#         contexto = {
#             'form':form
#         }
#         if form.is_valid():
#             form.save()
#             return redirect('index')

#     return render(request, 'create_currency.html',contexto)

# def editCurrency(request,id):
#     currency = Currency.objects.get(id = id)
#     if request.method == 'GET':
#         form = CurrencyForm(instance = currency)
#         contexto = {
#             'form':form
#         }
#     else:
#         form = CurrencyForm(request.POST, instance = currency)
#         contexto = {
#             'form':form
#         }
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     return render(request,'create_currency.html',contexto)


# def deleteCurrency(request,id):
#     currency = Currency.objects.get(id = id)
#     currency.delete()
#     return redirect('index')