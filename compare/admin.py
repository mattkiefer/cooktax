from models import Property
from django.db import models
from django.contrib import admin

class PropertyModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Property,PropertyModelAdmin)
