from django.db import models
from tinymce.models import HTMLField
class service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_desc = HTMLField()
# Create your models here.
