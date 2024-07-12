from django.contrib import admin
from .models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['task', 'description', 'completed', 'created', 'updated_at']
    list_filter = ['completed', 'created', 'updated_at']
    search_fields = ['task', 'description']

admin.site.register(Todo, TodoAdmin)