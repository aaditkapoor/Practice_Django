from django.contrib import admin
from Models.models import Box
# Register your models here.

class Set(admin.ModelAdmin):
	fields = ['date','firstname']

admin.site.register(Box,Set)
