from django.db import models

# Create your models here.
class PortfolioTransaction(models.Model):
    datetime = models.DateTimeField()
    equityType = models.CharField(max_length=10)
    equityName = models.CharField(max_length=30)
    units = models.DecimalField(max_digits=20, decimal_places=10)
    currency = models.CharField(max_length=10)