from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_admin', 'is_staff', 'is_active', 'date_joined')
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined', 'password') 

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'username', 'email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_admin', 'is_superuser', 'is_staff', 'is_active')
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('password',)
        return self.readonly_fields
