from django.db import models

# Create your models here.

class qrcode(models.Model):
    data = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='qrcodes/')

    def __str__(self):
        return self.data
    

