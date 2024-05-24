from django.contrib import admin # type: ignore

# Register your models here.
from .models import *
admin.site.register(qrcode)
admin.site.register(userAccount)