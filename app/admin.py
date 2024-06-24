from django.contrib import admin
from . import models, views

# Register your models here.
class UrlAdmin(admin.ModelAdmin):
    list_display = ('id','ourl','furl')

admin.site.register(models.Urls,UrlAdmin)