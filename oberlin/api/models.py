from django.db import models

class College(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    about = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
