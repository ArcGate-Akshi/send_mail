from django.db import models
# from customer import Customer
# from message import Message
from .message import Message
from .customer import Customer

STATUS = (
    (0, "unsent"),
    (1, "sent")
)


class Delivery(models.Model):
    d_id = models.BigAutoField(primary_key=True)
    status = models.IntegerField(choices=STATUS, default=0)
    email_pk = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, default='1')
    message_pk = models.ForeignKey(Message, on_delete=models.CASCADE, default=" ")

    # def __str__(self):
    #     return self.status

    class Meta:
        db_table = 'delivery'
