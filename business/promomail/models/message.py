from django.db import models


class Message(models.Model):
    m_id = models.BigAutoField(primary_key=True, default='00')
    subject = models.CharField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return self.m_id

    class Meta:
        db_table = 'message'
