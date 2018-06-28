from django.contrib import admin
from .models import Operator, SIM, Guest
# Register your models here.
admin.site.register(Operator)
admin.site.register(SIM)
admin.site.register(Guest)