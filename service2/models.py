from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class service(models.Model):
    service_title = models.CharField(max_length=50)
    service_desc = HTMLField()
    image_field = models.FileField(upload_to="new/", max_length=250,null=True,default=None)
    slug_name = AutoSlugField(populate_from='service_title',unique=True,default=None,null=True)
# Create your models here.

class savedata(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    email = models.CharField(max_length=50)
    address = models.TextField()