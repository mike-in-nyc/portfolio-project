from django.contrib import admin

# Register your models here.
from .models import job #current directory

admin.site.register(job)