from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addPortfolio', views.addPortfolioTransaction, name='addPortfolio'),
]