from django.shortcuts import render
from . models import Stock,PurchaseProduct,Purchase,Profit
from products.models import ProductData
from django.core import serializers
from django.http import HttpResponse
from products.models import ProductData,ProductSizeData
from home.models import CategoryData
from sub_category.models import SubCategoryData
from place_order.models import OrderDetailsData,OrderData
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal
import datetime
import json


# used to add data to the model Stock with some default values
#for product in ProductData.objects.all():
#    obj = Stock()
#    obj.product_name_id = product.id
#    obj.units = 0
#    obj.save()


order_id = "7Q0N2657"
profit = 0.0
def add_profit_data(order_id,units_buy=0.0,orders = []):
    if units_buy == 0.0 :
        orders = OrderDetailsData.objects.filter(order_id=order_id)
    for order in orders :
        if units_buy == 0.0 :
            units_to_buy = find_units(order.size,order.unit,order.quantity)
        else:
            units_to_buy = units_buy

        id = order.product_id
        detail = unit_checker(order.size, order.unit, order.discounted_price)
        size, unit, sp = detail[0], detail[1], detail[2]
        
        cost_ranges = PurchaseProduct.objects.filter(product_id=id)
        cost_ranges = sorted(cost_ranges,key= lambda x: x.created)
        for cost_row in cost_ranges:
            if cost_row.units_left_to_be_sold != 0.0 :
                PROFIT = cost_row.profit
                curr_units = cost_row.units_left_to_be_sold
                ## check if the first created 'units' field in purchaseproduct table
                ## is greater than the 'units' that the purchase is being made
                if curr_units >= units_to_buy:
                    ##print("cost price for ",order.name, "is ",cost_row.cost_price)
                    stock = Stock.objects.filter(product_id=id)[0]

                    if float(size) < float(stock.units):
                        PROFIT += float(units_to_buy * (sp-cost_row.cost_price))
                        #print("Profit for",order.name," is Rs.", PROFIT)
                        cost_row.units_left_to_be_sold -= units_to_buy
                        cost_row.profit = PROFIT
                        cost_row.save()
                        print(order.name,cost_row.units_left_to_be_sold)
                        break
                    else:
                        print("Cannot buy not enough stock", order.name)
                        break
                else:   ## update 'units' in PurchaseProducts to 0 and evaluate profit from next data entry in cost_ranges table
                    #print(order.name,'is an exception  ',curr_units,' : ',units_to_buy)
                    units_left = float(units_to_buy-curr_units)
                    cost_row.profit += float(curr_units * (sp-cost_row.cost_price))
                    cost_row.units_left_to_be_sold = 0.0
                    cost_row.save()
                    add_profit_data(order_id,units_left,[order])
                    break




def find_units(size,unit,quantity):
    size = int(size)
    quantity = int(quantity)
    if unit=='ml' or unit=='gms':
        return (quantity*size)/float(1000)
    else:
        return (quantity*size)

def unit_checker(size,unit,price):
    if unit == 'gms' :
       return ([size/float(1000),'Kg',(price/float(size))*1000])
    elif unit == 'ml' :
        return ([size/float(1000),'Lt',(price/float(size))*1000])
    elif unit == 'Kg':
        return ([size,'Kg',price/float(size)])
    elif unit == 'Lt' :
        return ([size,'Lt',price/float(size)])
    else:
        return ([size,unit,price/float(size)])

def getstock(request , subcategoryid):

    for x in ProductSizeData.objects.all():
        print(x.unit)
    print('hello')
    subcategoryid = int(subcategoryid)

    if request.method == 'GET':
        if request.user.is_authenticated():
            print('Successful')
            products = ProductData.objects.all()
            stocks = Stock.objects.all()
            categories = CategoryData.objects.all()
            subcategories = SubCategoryData.objects.all()
            print(subcategoryid)
            return render(request , 'inventory/stock.html',
                          {'products':products,
                           'user':request.user,
                           'stocks':stocks,
                           'categories': categories,
                           'subcategories': subcategories,
                           'subcategoryid':subcategoryid
                           })

        else:
            print('Not authenticated')
            return None
    else:
        print('Not get method')
        return None


def test(request):
    age = 33
    return render(request,'inventory/test.html',{'age':age})


def stockjson(request):
    stocks = Stock.objects.all()
    queryset = serializers.serialize('json',stocks)
    return HttpResponse(queryset,content_type='application/json')

def processedproducts(request):
    products = ProductData.objects.all()
    product_ranges = ProductSizeData.objects.all()
    products_list = {};
    for product in products:
        units = []
        for product_row in product_ranges:
            if product.id == product_row.product_id :
                units.append({'size':product_row.size,
                              'unit':product_row.unit})
        products_list[product.id] = {'units':units,
                                    'name':product.name,
                                     'id':product.id}

    return HttpResponse(json.dumps(products_list),content_type='application/json')


def purchase(request):
    if request.user.is_authenticated():
        if request.method == "POST":
           name = request.POST.getlist('name')
           product_id = request.POST.getlist('product_id')
           unit = request.POST.getlist('unit')
           size = request.POST.getlist('size')
           cost_price = request.POST.getlist('cost_price')
           quantity = request.POST.getlist('quantity')
           total = request.POST.getlist('total')
           for i in range(len(name)-1):
               if total[i] == "" :
                   print("That's not an int!")
                   status = "Something wrong with your data"
                   return render(request, 'inventory/purchase.html', {'user': request.user,
                                                                      'date': str(datetime.date.today()),
                                                                      'status': status
                                                                      })
               if total[i] == "0" :
                   status = "Sorry ! Can't purchase something for Rs. 0"
                   return render(request, 'inventory/purchase.html', {'user': request.user,
                                                                  'date': str(datetime.date.today()),
                                                                  'status':status
                                                                  })
           spent = 0.0
           for i in range(len(name)-1):
               update_stock(product_id[i],unit[i],quantity[i],size[i])
               purchase = PurchaseProduct()
               purchase.name = name[i]
               purchase.product_id = product_id[i]
               purchase.unit = unit[i]
               purchase.size = int(size[i])
               purchase.cost_price = cost_price[i]
               purchase.quantity = int(quantity[i])
               purchase.total = total[i]
               purchase.save()
               purchase.units_left_to_be_sold = purchase.units
               purchase.save()
               spent += float(purchase.total)
           buy = Purchase()
           buy.total = spent
           buy.number = i+1
           buy.save()
           status = " Products have been purchased ! "
           return render(request, 'inventory/purchase.html', {'user': request.user,
                                                              'date': str(datetime.date.today()),
                                                              'status':status,
                                                              'success': True
                                                              })

        else:
            return render(request,'inventory/purchase.html',{'user':request.user,
                                                             'date':str(datetime.date.today()),
                                                             })
    else:
        print('Admin not logged in !')
        return None


def update_stock(id,unit,quantity,size):  ## updates stock and returns the units(floating number)
    id = int(id)
    quantity = int(quantity)
    size = int(size)
    stock = Stock.objects.get(product_id=id)
    print(stock.name)
    if unit == 'ml' or unit=='gms' :
        stock.units += Decimal((quantity*size)/float(1000))
        print("Stock updated")
    else:
        stock.units += (quantity * size)
        print('Stock updated')
    stock.save()


#def productranges(request):
#    queryset = ProductSizeData.objects.values('product_id','name','name__name','unit','size')
#    serialized_q = json.dumps(list(queryset), cls=DjangoJSONEncoder)
#    return HttpResponse(serialized_q,content_type='application/json')


def profit(request):
    if request.user.is_authenticated():
        print('Profit function')
        add_profit_data(order_id)
        return render(request,'inventory/profit.html')
    else :
        return HttpResponse(request,'admin_panel/order/order_details.html')



















