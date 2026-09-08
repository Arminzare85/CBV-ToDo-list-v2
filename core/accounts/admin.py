from django.contrib import admin
from .models import Profile

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user__email', 'is_verified')
    search_fields = ('full_name', 'user__email')
    ordering = ('is_verified',)

admin.site.register(Profile, AccountAdmin)