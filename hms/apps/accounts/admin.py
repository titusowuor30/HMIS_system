from django.contrib import admin
from .models import Student,Guest,Hostel_manager,User,Role,Profile


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name','phone','course')

admin.site.register(Student,StudentAdmin)

class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name','phone')

admin.site.register(Guest,GuestAdmin)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('manager_name','phone')

admin.site.register(Hostel_manager,ManagerAdmin)

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Profile)