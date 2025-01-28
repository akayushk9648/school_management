from django.contrib import admin
from .models import *


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number')
    search_fields = ('name', 'address','contact_number')
    list_filter = ('name',)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('organization', 'recipient_name', 'amount', 'description')
    search_fields = ('recipient_name', 'organization__name')
    list_filter = ('organization',)


class FeeAdmin(admin.ModelAdmin):
    list_display=('fee_id','tenant','student','fee_type','amount','due_date','status')
    search_fields=('fee_id','tenant','student','fee_type','amount','due_date','status')
    list_filter=('fee_id',)
    readonly_fields=('fee_id',)

admin.site.register(Fee,FeeAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Receipt, ReceiptAdmin)