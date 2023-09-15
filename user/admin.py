from django.contrib import admin
from . models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=("id","pname","pprice","dprice","pimage","pdesc","date","pcolor","pcategory")
admin.site.register(Product, ProductAdmin)

class mcategoryAdmin(admin.ModelAdmin):
    list_display=("id","Name","CPic")
admin.site.register(mcategory, mcategoryAdmin)


class maincategoryAdmin(admin.ModelAdmin):
    list_display =("id","Name","Mpic")
admin.site.register(maincategory,maincategoryAdmin)

class registerAdmin(admin.ModelAdmin):
    list_display = ("Name","Address","Mob","Email","Password")
admin.site.register(register,registerAdmin)