from django.contrib import admin
from .models import Machine, Personnel, infrastructure


# Register your models here.
admin.site.register(Machine)
admin.site.register(Personnel)
admin.site.register(infrastructure)