from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Ticket

# Register your models here.
admin.site.unregister(User)

@admin.register(Ticket)
class GeneralAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_no', 'email', 'quantity', 'seats')
    pass

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin, ImportExportModelAdmin):
    list_display = ('username', 'last_login', 'date_joined', 'is_staff')
    pass