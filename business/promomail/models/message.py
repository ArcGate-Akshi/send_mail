from django.db import models


class Message(models.Model):
    m_id = models.CharField(primary_key=True, default='mail1', blank=False, max_length=20)
    subject = models.CharField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return self.m_id

    class Meta:
        db_table = 'message'
