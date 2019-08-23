# django
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General information', {
            'fields': ('uuid', 'name', 'type', 'price')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Audit data', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')
        })
    )

    list_display = ('name', 'type', 'price', 'status', 'created_at')
    search_fields = ['name', 'price']
    list_filter = ['type']
    ordering = ('name', 'price', 'created_at')

    readonly_fields = ['id', 'uuid', 'created_at', 'updated_at', 'created_by', 'updated_by']
