
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    country= models.CharField(db_column='country', max_length=100, blank=False)
    year = models.IntegerField(db_column='year',blank=False, default=2000)
    file = models.FileField(upload_to='uploads/')

