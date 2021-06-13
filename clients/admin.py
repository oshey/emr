from django.contrib import admin

# Register your models here.
from clients.models import Client, Branch

admin.site.register(Client)
admin.site.register(Branch)
