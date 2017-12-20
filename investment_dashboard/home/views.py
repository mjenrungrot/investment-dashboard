from django.shortcuts import render
from django.http import HttpResponse

from portfolio.views import getPortfolioContext

# Create your views here.
def index(request):
    context = getPortfolioContext()
    return render(request, 'home/index.html', context=context)