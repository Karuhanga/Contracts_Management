from django.contrib import admin
from .models import Contract, Section, ContractManager


admin.site.site_header = "Contracts Management"

# Register your models here.
admin.site.register(Contract)
admin.site.register(Section)
admin.site.register(ContractManager)
