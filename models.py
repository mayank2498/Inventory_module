from __future__ import unicode_literals

from django.db import models
from products.models import ProductData , ProductSizeData
from place_order.models import OrderData,OrderDetailsData

class Stock(models.Model):
    product_name = models.ForeignKey(ProductData,null=True)
    product_id = models.IntegerField(null=False)
    subcategory_id = models.IntegerField(null=False,default=0)
    units = models.DecimalField(default=0,decimal_places=2,max_digits=50)
    measured_unit = models.CharField(max_length=500,null=True,default='Kg')
    name = models.CharField(max_length=500,null=True)
    image = models.CharField(max_length=500,null=True,default='/media/welcome/Veg_World.png')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False,auto_now=True)

    def save(self,*args,**kwargs):
        self.product_id = self.product_name.id
        self.name = self.product_name.name
        self.image = self.product_name.image.url
        self.subcategory_id = self.product_name.sub_category_id
        product_ranges = ProductSizeData.objects.all()
        for product_row in product_ranges:
            if product_row.product_id == self.product_id :
                if product_row.unit == 'gms':
                    self.measured_unit = 'Kg'
                    break
                elif product_row.unit == 'ml':
                    self.measured_unit = 'Lt'
                    break
                else:
                    self.measured_unit = product_row.unit
                    break
            else:
                continue
        print(self.measured_unit)

        super(Stock,self).save(*args,**kwargs)

class PurchaseProduct(models.Model):
    product_id = models.IntegerField(default=0)
    name = models.CharField(max_length=500,default="NoName")
    cost_price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(default=0,decimal_places=2,max_digits=100)
    unit = models.CharField(max_length=100,default='Kg')  ## stores Kg,Lt,packets,box
    units = models.FloatField(default=0)                  ## stores float number ex 25.78 KG
    units_left_to_be_sold = models.FloatField(default=0)
    profit = models.FloatField(default=0)
    size = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    modified = models.DateTimeField(auto_now_add=False,auto_now=True)

    ## evaluate 'units' field whenever a PurchaseProduct object is saved
    def save(self,*args,**kwargs):
        if self.unit == 'ml' or self.unit == 'gms' :
            self.units = (self.size * self.quantity )/float(1000)
        else:
            self.units = (self.size * self.quantity)
        super(PurchaseProduct,self).save(*args,**kwargs)


class Purchase(models.Model):
    total = models.DecimalField(default=0,decimal_places=2,max_digits=100)
    number = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False, auto_now=True)

class Profit(models.Model):
    orderdata = models.ForeignKey(OrderData,null=False)
    bill = models.FloatField(default=0)
    profit = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    def save(self,*args,**kwargs):
        self.bill = self.orderdata.total_bill
        super(Profit,self).save(*args,**kwargs)








