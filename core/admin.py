from django.contrib import admin
from .models import *

# Register your models here.
class TenantAdmin(admin.ModelAdmin):
    list_display=('tenant_id','school_name','address','contact_email','contact_phone','created_at','updated_at')
    search_fields=('tenant_id','school_name','address','contact_email','contact_phone','created_at','updated_at')
    list_filter=('tenant_id',)
    readonly_fields=('tenant_id',)

class UserAdmin(admin.ModelAdmin):
    list_display=('user_id','tenant','name','email','password','role','status','created_at','updated_at')
    search_fields=('user_id','tenant','name','email','role','status','created_at','updated_at')
    list_filter=('user_id',)
    readonly_fields=('user_id',)


admin.site.register(Tenant,TenantAdmin)
admin.site.register(User,UserAdmin)