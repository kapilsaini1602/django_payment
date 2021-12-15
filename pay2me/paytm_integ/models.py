from django.db import models


# Create your models here.
class OrderDetails(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    ammount = models.IntegerField()
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.username
