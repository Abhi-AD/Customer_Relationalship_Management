from django.contrib import admin
from cms_app.models import (
    Service_Category,
    Sub_Category,
    AddMember,
    DisplayProfile,
    Plan_Subscription,
    User_Subscription,
    Attendance,
    CashTransaction,
    Inventory,
    InventoryBalance,   
    Contact, 
    
)

# from cms_app.models import  UserSubscription,Subscription,Price,Product


# Register your models here.
admin.site.register(Service_Category)
admin.site.register(Sub_Category)
admin.site.register(AddMember)
admin.site.register(DisplayProfile)
admin.site.register(Plan_Subscription)
admin.site.register(User_Subscription)
admin.site.register(Attendance)
admin.site.register(CashTransaction)
admin.site.register(Inventory)
admin.site.register(InventoryBalance)
admin.site.register(Contact)
# admin.site.register(Images)
