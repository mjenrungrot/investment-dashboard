from django import forms

class PortfolioTransactionForm(forms.Form):
    datetime = forms.DateTimeField()
    equityType = forms.CharField(max_length=10)
    equityName = forms.CharField(max_length=30)
    units = forms.DecimalField(max_digits=20, decimal_places=10)
    currency = forms.CharField(max_length=10)
