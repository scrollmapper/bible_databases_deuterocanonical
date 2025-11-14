from django.contrib import admin
from .models import Bot


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    """
    Admin configuration for Bot model.
    """
    list_display = [
        'name', 
        'crawler_type', 
        'last_run_at', 
        'pages_fetched', 
        'obey_robots_txt',
        'created_at'
    ]
    list_filter = ['crawler_type', 'obey_robots_txt', 'autothrottle_enabled']
    search_fields = ['name', 'user_agent']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'crawler_type')
        }),
        ('Crawler Settings', {
            'fields': (
                'user_agent',
                'download_delay',
                'concurrent_requests',
                'obey_robots_txt',
                'autothrottle_enabled',
                'cookies_enabled'
            )
        }),
        ('Statistics (Read-Only)', {
            'fields': ('last_run_at', 'pages_fetched', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    readonly_fields = ['last_run_at', 'pages_fetched', 'created_at', 'updated_at']
