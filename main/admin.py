from django.contrib import admin
from main.models import Students
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)

admin.site.register(Students, StudentAdmin)
