from django.contrib import admin
from .models import Pensiune, Activitate, Restaurant, Transport

# Register your models here.
admin.site.register(Pensiune)
admin.site.register(Activitate)
admin.site.register(Restaurant)
admin.site.register(Transport)
