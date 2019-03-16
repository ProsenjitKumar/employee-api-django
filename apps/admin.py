from django.contrib import admin
from .models import Employeer


class EmpoyeeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Employeer, EmpoyeeAdmin)