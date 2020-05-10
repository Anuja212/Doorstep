from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from stock.models import register
from stock.models import Product1
from stock.models import order1
from stock.models import availableproduct
from django.utils import timezone
import datetime
from operator import itemgetter 
from django.db.models import F
# Create your views here.


def home(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello world")

def about(request):
    return render(request,'about.html')
def login(request):

    if request.method == 'POST':
        username = request.POST['Username']
        password1 = request.POST['Password']
        user = auth.authenticate(username=username, password=password1)
        if username == 'admin' and password1 == '123':
            return redirect('admin1/')
        if user is not None:
            auth.login(request, user)
            return redirect('customer/')
        else:
            return render(request, 'login.html', {"message": "Invalid Credential"})
    else:
        return render(request, 'login.html')


def Registration(request):
    if request.method == 'POST':
        customerid = request.POST['generate']
        print(type(customerid))
        firstname = request.POST['Firstname']
        lastname = request.POST['Lastname']
        username = request.POST['Username']
        password = request.POST['Password']
        phone = request.POST['Phoneno']
        address = request.POST['Address']
        if address == "Tathwade" or address == "Hinjewadi" or address == "Nawale" or address == "Wakad" or address == "Kalewadi":
            user = User.objects.create_user(
                username=username, password=password)
            o_ref = register(customer_id=customerid, First_Name=firstname,
                             Last_Name=lastname, Address=address, Phone_No=phone)
            o_ref.save()
            user.save()
            return render(request, 'registration.html', {"message": "Registred"})
        else:
            return render(request, 'registration.html', {"message": "Service is not Available"})

    else:
        return render(request, 'registration.html')


def admin1(request):

    query_results = availableproduct.objects.all()
    return render(request, 'admin.html', {'Result': query_results})


def customer(request):
    query_results = Product1.objects.all()
    return render(request, 'customer.html', {'Result': query_results})


def add(request):
    if request.method == 'POST':
        Product_No = request.POST.get("Product_Id")
        Product_Name = request.POST.get("Product_Name")
        Quantity = request.POST.get("Quantity")
        Price1 = request.POST.get("Cost_Price")
        Price2 = request.POST.get("Total_cost_Price")
        Price3 = request.POST.get("Selling_Price")
        Price4 = request.POST.get("Total_Selling_Price")
        # now = datetime.datetime.now().date()
        o_ref = Product1(Date=datetime.datetime.now().date(), Product_No=Product_No, Product_Name=Product_Name, Quantity=Quantity,
                         Cost_Price=Price1, Tot_Cost_Price=Price2, Selling_Price=Price3, Tot_selling_Price=Price4)

        o_ref.save()
        o = availableproduct(Product_No=Product_No,
                             Product_Name=Product_Name, Quantity=Quantity)
        o.save()
        return render(request, 'add.html', {"message": "Product Added"})
    else:

        return render(request, 'add.html')


def delete(request):
    if request.method == 'POST':
        Product_No = request.POST.get("Product_Id")
        Product1.objects.filter(Product_No=Product_No).delete()
        availableproduct.objects.filter(Product_No=Product_No).delete()
        return render(request, 'delete.html', {"message": "Record Deleted"})
    else:

        return render(request, 'delete.html')


def available(request):
    query_results = Product1.objects.all()
    return render(request, 'available.html', {'Result': query_results})


def update(request):
    if request.method == 'POST':
        Product_No = request.POST.get("Product_Id")
        p1 = int(Product_No)
        query_results = Product1.objects.all().filter(Product_No=p1)
        no = p1
        return render(request, 'find.html', {'no': no, 'Result': query_results, "message": "Product Search successfully"})

    else:
        return render(request, 'update.html')


def modify(request):
    if request.method == 'POST':
        Product_No = request.POST.get("Product_Id")
        Product_Name = request.POST.get("Product_Name")
        Quantity = request.POST.get("Quantity")
        Price1 = request.POST.get("Cost_Price")
        Price2 = request.POST.get("Total_cost_Price")
        Price3 = request.POST.get("Selling_Price")
        Price4 = request.POST.get("Total_Selling_Price")
        now = datetime.datetime.now().date()
        Product1.objects.filter(Product_No=Product_No).update(Date=now, Product_Name=Product_Name, Quantity=Quantity,
                                                              Cost_Price=Price1, Tot_Cost_Price=Price2, Selling_Price=Price3, Tot_selling_Price=Price4)
        availableproduct.objects.filter(Product_No=Product_No).update(
            Product_No=Product_No, Product_Name=Product_Name, Quantity=Quantity)

        return render(request, 'update.html', {"message": "Product Updated"})
    else:
        return render(request, 'update.html')


def Info(request):
    query_results = Product1.objects.all()
    return render(request, 'Info.html', {'Result': query_results})


def order(request):
    id_no = 0
    query_results = Product1.objects.all()

    for data in query_results:
        data.id_no = id_no
        print("quantity is")
        print(data.Quantity)
        id_no += 1
    name = 'Product Information'
    return render(request, 'order.html', {'name': name, 'Result': query_results})


def customerdetail(request):
    query_results = register.objects.all()
    return render(request, 'customerdetail.html', {'Result': query_results})


def find(request, id_no):
    d = id_no

    query_results = Product1.objects.all()
    id_no = 0
    for data in query_results:
        data.id_no = id_no
        id_no += 1
    name = 'Product Information'
    if request.method == 'POST':
        Product_No = request.POST.get("pro_"+d)
        Product_Name = request.POST.get("Product_Name_"+d)
        Quantity1 = request.POST.get("qty_"+d)
        na1 = availableproduct.objects.filter(Product_Name=Product_Name).values_list('Quantity')
        var1 = itemgetter(0)(na1) 
        customerid = request.POST.get("customerid")
        datepicker = request.POST.get("datepicker")

        Q1 = int(Quantity1)

        Price3 = request.POST.get("sel_"+d)
        Price4 = request.POST.get("total_"+d)
        now = datetime.datetime.now().date()
        print(str(var1[0]))
        
        if int(Quantity1) > int(var1[0]):
        
            name1 = 'Avaliable Quantity is only '
            Quant=int(var1[0])
            return render(request, 'order.html', {'name': name, 'customerid': customerid, 'datepicker': datepicker, 'Result': query_results,'name1':name1,'Quant':Quant})       
        else:
            availableproduct.objects.filter(Product_Name=Product_Name).update(Quantity=F('Quantity') - Quantity1)
        o_ref = order1(Order_Date=now, Product_No=Product_No, customer_id=customerid, Product_Name=Product_Name,
                       Quantity=Quantity1, Selling_Price=Price3, Delivery_Date=datepicker, Total=Price4)
        o_ref.save()
        return render(request, 'order.html', {'name': name, 'customerid': customerid, 'datepicker': datepicker, 'Result': query_results})

def show(request):
    id_no = 0
    # query_results = order1.objects.all()
    if request.method == 'POST':
        now = datetime.datetime.now().date()
        customerid = request.POST.get("customerid")
        query_results = order1.objects.filter(
            customer_id=customerid, Order_Date=now).all()
    for data in query_results:
        data.id_no = id_no
        id_no += 1

    name = 'Product Information'

    return render(request, 'show.html', {'name': name, 'Result': query_results})


def delorder(request, id_no):
    d = id_no
    query_result = order1.objects.all()
    if request.method == 'POST':
        Product_No = request.POST.get("pro_"+d)
        Product_Name = request.POST.get("Product_Name_"+d)

        Quantity1 = request.POST.get("qty_"+d)

        order1.objects.filter(Product_No=Product_No).delete()
        availableproduct.objects.filter(Product_Name=Product_Name).update(
            Quantity=F('Quantity') + Quantity1)
    id_no = 0
    for data in query_result:
        data.id_no = id_no
        print("Hello")
        id_no += 1
    name = 'Order Information'
    return render(request, 'show.html', {'name': name, 'Result': query_result})


def orderdetail(request):
    now = datetime.datetime.now().date()
    query_result = order1.objects.filter(Delivery_Date=now).all()

    return render(request, 'orderdetail.html', {'Result': query_result})


def search(request):
    # query_results = register.objects.all()
    if request.method == 'POST':
        customerid = request.POST.get("customerid")
        query_results = register.objects.filter(customer_id=customerid).all()
        print(query_results)

        return render(request, 'customerdetail.html', {'Result': query_results})
    else:
        query_results = register.objects.all()
        return render(request, 'customerdetail.html', {'Result': query_results})


def history(request):
    query_result = order1.objects.all()
    name = 'Order Information'
    return render(request, 'history.html', {'name': name, 'Result': query_result})


def serachhistory(request):
    name = 'Order Information'
    if request.method == 'POST':
        customerid = request.POST.get("customerid")
        query_results = order1.objects.filter(customer_id=customerid).all()
    

        return render(request, 'searchhistory.html', {'name': name, 'Result': query_results})
    else:
        query_results = register.objects.all()
        return render(request, 'history.html', {'name': name, 'Result': query_results})


def view(request):

    query_results = Product1.objects.all()
    return render(request, 'view.html', {'Result': query_results})
