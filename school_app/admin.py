from django.contrib import admin
from .models import *

admin.site.register(School)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Subject)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = [
        "fio",
    	"clss"
    ]
    search_fields = ["fio"]
    list_filter = ("clss",)