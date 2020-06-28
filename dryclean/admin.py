from django.contrib import admin

# Register your models here.
from dryclean.models import pricing
 
@admin.register(pricing)
class pricingAdmin(admin.ModelAdmin):
    pass