from django.contrib import admin

from . import models

admin.site.register(models.Parent)
admin.site.register(models.Child)
