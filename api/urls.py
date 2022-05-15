from django.urls import path
from . import views

urlpatterns = [
    path('divise', views.divise, name='divise'),
    path('divise/<int:id>', views.divise, name='divise')
]
