from django.db import models


class Customer(models.Model):
    cid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False, default=' ',unique=True)
    contact = models.CharField(max_length=10, default='000')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customer'
