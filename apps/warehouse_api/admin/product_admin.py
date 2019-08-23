# django
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General information', {
            'fields': ('external_id', 'first_name', 'last_name', 'email')
        }),
        ('Advisor profile', {
            'fields': ('user', 'firm',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Privileges', {
            'fields': ('all_clients_privilege',)
        }),
        ('Audit data', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')
        })
    )

    list_display = ('full_name', 'email', 'user', 'firm', 'clients_privilege', 'created_at')
    search_fields = ['first_name', 'last_name', 'email']
    ordering = ('first_name',)

    readonly_fields = ['id', 'external_id', 'created_at', 'updated_at', 'created_by', 'updated_by']