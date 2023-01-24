from django.db import models
from django.utils.translation import gettext_lazy as _

class Data(models.Model):
    nim = models.IntegerField(primary_key= True)
    nama = models.CharField(max_length=20)
    alamat = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Meta:
    db_table = 'data'
    