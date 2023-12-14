from django.contrib import admin
from.models import Departmentss,Doctor,appointmet
# Register your models here.
admin.site.register(Departmentss)
admin.site.register(Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','name','phone','email','doc_name','booked_date')
admin.site.register(appointmet,BookingAdmin)