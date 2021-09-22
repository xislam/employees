from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from employees.models import Departments, Employee

admin.site.register(
    Departments,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(Employee)
