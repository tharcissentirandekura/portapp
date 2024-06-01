from django.db import models # type: ignore

# Create your models here.

class qrcode(models.Model):
    data = models.CharField(max_length = 255)
    image = models.ImageField(upload_to='qrcodes/')

    def __str__(self):
        return self.data

class userAccount(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.username



