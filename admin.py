from django.contrib import admin
from .models import *
# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ["product_name","units","measured_unit",'id','product_id']
    # fields=["id","name","price","discounted_price","unit","size"]
    # fields=["category_name","sub_category_name","image_","name","description","image","size","price","discounted_price","unit"]
    readonly_fields = ['product_id']


class PurchaseProductAdmin(admin.ModelAdmin):
    list_display = ["name",'size',"unit","quantity",'total','cost_price','created','units','units_left_to_be_sold','profit']
    readonly_fields = ['product_id']

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["number",'total','created']


admin.site.register(Stock,StockAdmin)
admin.site.register(PurchaseProduct,PurchaseProductAdmin)
admin.site.register(Purchase,PurchaseAdmin)