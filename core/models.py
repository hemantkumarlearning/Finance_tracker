from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    TYPE_CHOICES = (('income','Income'),('expense','Expense'))
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10,choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    monthly_limit = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()

