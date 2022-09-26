from django.contrib import admin
from .models import GujratAccount, LahoreAccount, MultanAccount, RawalpindiAccount, FaislabadJhungAccount, GujranwalaAccount, LahoreWeeklyClosing
from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(GujratAccount)
class GujratAccountAdmin(admin.ModelAdmin):
   list_display = ['Date', 'VIA', 'Truck_Number', 'Truck_Company', 'Total_CTN', 'To_Pay', 'Truck_Rent', 'Karachi_Transit_Rent', 'Lahore_Transit_Rent']
   search_fields = ['Date', 'VIA', 'Truck_Number', 'Truck_Company', 'Total_CTN', 'To_Pay', 'Truck_Rent', 'Karachi_Transit_Rent', 'Lahore_Transit_Rent']
   list_filter = ['Date', 'VIA', 'Truck_Number', 'Truck_Company']
   date_hierarchy = 'Date'
   pass


@admin.register(LahoreAccount)
class LahoreAccountAdmin(admin.ModelAdmin):
   list_display = ['Date','Delivery_Day', 'Truck_Number', 'Truck_Company', 'Total_CTN', 'To_Pay', 'Truck_Rent','Payment_Date','Amount']
   search_fields = ['Date', 'Truck_Number', 'Truck_Company', 'Total_CTN', 'To_Pay', 'Truck_Rent']
   list_filter = ['Date', 'Truck_Number', 'Truck_Company']
   date_hierarchy = 'Date'
   pass


@admin.register(MultanAccount)
class MultanAccountAdmin(admin.ModelAdmin):
   list_display = ['Date', 'VIA', 'Truck_Number', 'Truck_Company', 'Total_CTN', 'To_Pay', 'Truck_Rent', 'Karachi_Transit_Rent']
   search_fields = ['Date', 'VIA', 'Truck_Number', 'Truck_Company', 'Total_CTN', 'To_Pay', 'Truck_Rent', 'Karachi_Transit_Rent']
   list_filter = ['Date', 'VIA', 'Truck_Number', 'Truck_Company']
   date_hierarchy = 'Date'
   pass


@admin.register(RawalpindiAccount)
class RawalpindiAccountAdmin(admin.ModelAdmin):
   list_display = ['Date', 'VIA', 'Truck_Number', 'Truck_Company', 'Total_CTN', 'To_Pay', 'Truck_Rent', 'Karachi_Transit_Rent', 'Lahore_Transit_Rent']
   search_fields = ['Date', 'VIA', 'Truck_Number', 'Truck_Company', 'Total_CTN', 'To_Pay', 'Truck_Rent', 'Karachi_Transit_Rent', 'Lahore_Transit_Rent']
   list_filter = ['Date', 'VIA', 'Truck_Number', 'Truck_Company']
   date_hierarchy = 'Date'
   pass


@admin.register(FaislabadJhungAccount)
class FaislabadJhungAccountAdmin(admin.ModelAdmin):
   list_display = ['Date', 'VIA', 'Truck_Number', 'Truck_Company', 'Total_CTN', 'To_Pay', 'Truck_Rent', 'Karachi_Transit_Rent', 'Lahore_Transit_Rent', 'FSD_to_Jhung_Transit_Rent']
   search_fields = ['Date', 'VIA', 'Truck_Number', 'Truck_Company', 'Total_CTN', 'To_Pay', 'Truck_Rent', 'Karachi_Transit_Rent', 'Lahore_Transit_Rent', 'FSD_to_Jhung_Transit_Rent']
   list_filter = ['Date', 'VIA', 'Truck_Number', 'Truck_Company']
   date_hierarchy = 'Date'
   pass


@admin.register(GujranwalaAccount)
class GujranwalaAccountAdmin(admin.ModelAdmin):
   list_display = ['Date', 'VIA', 'Truck_Number', 'Truck_Company', 'Total_CTN', 'To_Pay', 'Truck_Rent', 'Karachi_Transit_Rent', 'Lahore_Transit_Rent','Rawalpindi_Transit_Rent']
   search_fields = ['Date', 'VIA', 'Truck_Number', 'Truck_Company', 'Total_CTN', 'To_Pay', 'Truck_Rent', 'Karachi_Transit_Rent', 'Lahore_Transit_Rent', 'Rawalpindi_Transit_Rent']
   list_filter = ['Date', 'VIA', 'Truck_Number', 'Truck_Company']
   date_hierarchy = 'Date'
   pass


@admin.register(LahoreWeeklyClosing)
class LahoreWeeklyClosingAdmin(admin.ModelAdmin):
    list_display =['start_date', 'end_date', 'Previous_Balance', 'Current_to_Pay','total_balance','Recovery','net_balance']
    pass

