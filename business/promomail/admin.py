from django.contrib import admin
from .models.customer import Customer
from .models.delivery import Delivery
from .models.message import Message


# Register your models here.
class AdminCustomer(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact', 'address', 'city', 'country']
    search_fields = ('name', 'city')





class AdminMessage(admin.ModelAdmin):
    list_display = ['m_id', 'subject', 'text']
    search_fields = ('m_id',)

class AdminDelivery(admin.ModelAdmin):
    list_display = ['d_id', 'status']
    search_fields = ('d_id', 'status')

# code for registering models
admin.site.register(Customer, AdminCustomer)

admin.site.register(Message, AdminMessage)
admin.site.register(Delivery, AdminDelivery)

