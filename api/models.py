from django.db import models

class Currency(models.Model):
    divise = models.CharField(max_length=25)
    usd_price = models.IntegerField()

    def __str__(self):
        return self.divise

    def to_json(self):
        return {
            'id': self.id, 
            'usd_price': self.usd_price,
            'divise': self.divise
        }