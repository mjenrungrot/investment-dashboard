from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.template import loader
from django.core import serializers
from .forms import PortfolioTransactionForm
from .models import PortfolioTransaction

from django.views.decorators.csrf import csrf_exempt

import pytz
import dateutil.tz
import datetime

@csrf_exempt
def addPortfolioTransaction(request):
    if request.method == "POST":
        form = PortfolioTransactionForm(request.POST)
        if form.is_valid():
            datetime = form.cleaned_data['datetime']
            equityType = form.cleaned_data['equityType']
            equityName = form.cleaned_data['equityName']
            units = form.cleaned_data['units']
            currency = form.cleaned_data['currency']
            instance = PortfolioTransaction.objects.create(datetime=datetime,
                                                           equityType=equityType,
                                                           equityName=equityName,
                                                           units=units,
                                                           currency=currency,)
            outputResponse = serializers.serialize('json', [instance])
            return HttpResponse(outputResponse, content_type='application/json')
        else:
            return HttpResponseBadRequest("Incorrect form. (Expected PortfolioTransaction form)")
    raise Http404("Incorrect method. (Expected POST)")

def getPortfolioContext():
    context = {}

    portfolioObjectParser = lambda portfolioObject: {
        "label": "{:}/{:}".format(portfolioObject.equityType, portfolioObject.equityName), 
        "equity": portfolioObject.units
    }
    allPortfolioTransactions = [portfolioObjectParser(object) for object in list(PortfolioTransaction.objects.all())]
    
    totalEquity = 0
    for transaction in allPortfolioTransactions: totalEquity += float(transaction["equity"])
    for idx in range(len(allPortfolioTransactions)): 
        allPortfolioTransactions[idx]["y"] = float(allPortfolioTransactions[idx]["equity"]) / totalEquity * 100.0
        del allPortfolioTransactions[idx]['equity']

    context['portfolio'] = allPortfolioTransactions
    currentUTCtime = datetime.datetime.now(pytz.utc)
    localTime = currentUTCtime.astimezone(dateutil.tz.tzlocal())
    context['title'] = 'Portfolio Allocation on ' + localTime.strftime("%B %d, %Y %H:%M %z")

    return context

def index(request):
    template = loader.get_template('portfolio/index.html')
    context = getPortfolioContext()
    return HttpResponse(template.render(context, request))