from django.contrib import admin
from .models import Asset

# Register your models here.


class FixedAssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'acquired_on','functional_status','service_interval', 'last_service_date','service_status',)
    list_filter = ('category',)


admin.site.register(Asset,FixedAssetAdmin)