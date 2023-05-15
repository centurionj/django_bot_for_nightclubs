from django.contrib import admin
from .models import Day, Perfomace, Order, Club

# Register your models here.

# class DayAdmin(admin.ModelAdmin):
#     list_display = ('id', 'day_of_weak')

class PerfomaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'club', 'date', 'which_day_of_weak')

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'qr_code')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name_sername', 'club', 'date')

admin.site.register(Day)
admin.site.register(Club, ClubAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Perfomace, PerfomaceAdmin)
