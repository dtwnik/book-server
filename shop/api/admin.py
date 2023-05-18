from django.contrib import admin

from .models import *

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('buyers', 'arrived')
    list_filter = ('arrived',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Book)
admin.site.register(Deposite)

admin.site.site_url = "http://localhost:3000/"

