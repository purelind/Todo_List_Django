from django.contrib import admin
from todo_list.models import Todo


class TodoAdmin(admin.ModelAdmin):
    """以下变量必须为列表或元组"""
    list_display = ('user', 'todo', 'priority', 'flag', 'pubtime')
    list_filter = ('pubtime',)
    ordering = ('-pubtime',)  # pubtime时间倒序显示

admin.site.register(Todo, TodoAdmin)

