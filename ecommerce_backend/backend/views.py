from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login     
# Create your views here.

def ureg(request):
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        hname = request.POST['hname']
        place = request.POST['place']
        pincode = request.POST['pincode']
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        u = User.objects.create(username=uname, password=make_password(pwd))
        u.groups.add(Group.objects.get(name='User'))
        p=UserProfile(fname=fname,lname=lname,phone=phone,email=email,hname=hname,place=place,pincode=pincode,user_id=u.id)
        p.save()
        response={
                'status':'success',
                'uid':u.pk,
        }
        return JsonResponse(response)

def login_post(request):
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        user = authenticate(username=uname, password=pwd)
        response={
              'status':'pending'
        }
        if user:
            if user.groups.filter(name='User').exists():
                response={
                'status':'success',
                'type':'user',
                'uid': user.id,
                'message':'logged in as user'
                }
                print("logged in")
            else:
               response={
                'status':'error',
                'type':'admin',
                'message':'Incorrect username or password'
                }
               print("error")

        return JsonResponse(response)


def addproduct(request):
        pname = request.POST['pname']
        description = request.POST['description']
        price = request.POST['price']       
        image = request.FILES['image']
        fs = FileSystemStorage()
        img_url = fs.save(image.name, image)

        p=Products(pname=pname,description=description,price=price,image=img_url)
        p.save()
        response={
                'status':'success',
        }
        return JsonResponse(response)


def viewproduct(request,uid):
        data = []
        c=[]
        try:

                om=OrderMaster.objects.get(uid=uid,status='pending')
                c=OrderDetails.objects.filter(ordermaster_id=om.pk).values_list('pid',flat=True)
                print(c,'iiiiiiiiiiiiiiiiiiiiii')
        except:
              pass
        d = Products.objects.all()
        for i in d:
            if i.id in c:
                button="Added to Cart"
            else:
                button="Add to Cart"

            data.append({
            'id': i.pk,
            'pname': i.pname,
            'des': i.description,
            'price': i.price,
            'image': i.image.name,
            'button':button,
            })
        response={
                'status':'success',
                'data':data,
        }
        print(data)
        return JsonResponse(response)

def addtocart(request,pid,uid):
        p=Products.objects.get(id=pid)
        u=User.objects.get(id=uid)
        try:
                om=OrderMaster.objects.get(uid=u,status='pending')
                om.total=om.total+p.price
                om.save()
                od=OrderDetails(ordermaster_id=om.id,pid=p,quantity=1)
                od.save()
        except:
                o=OrderMaster(uid=u,total=p.price,status='pending',date=datetime.now())
                o.save()
                od=OrderDetails(ordermaster_id=o.id,pid=p,quantity=1)
                od.save()
        response={
                'status':'success',
        }
        return JsonResponse(response)

def viewcart(request,uid):
        data=[]
        try:
                om=OrderMaster.objects.get(uid=uid,status='pending')
                c=OrderDetails.objects.filter(ordermaster_id=om.pk)
                for i in c:
                        data.append({
                        'id': i.pk,
                        'pname': i.pid.pname,
                        'des': i.pid.description,
                        'price': i.pid.price,
                        'image': i.pid.image.name,
                        'quantity':i.quantity,
                        })
        except:
              pass
        
        response={
                'data':data,
                'status':'success',
        }
        return JsonResponse(response)

def updatequantity(request,oid,q):
        od=OrderDetails.objects.get(id=oid)
        od.quantity=od.quantity+int(q)
        od.save()
        if od.quantity < 1:
            od.quantity = 1
            od.save()
        else:
                om=OrderMaster.objects.get(id=od.ordermaster.pk)
                om.total=om.total+(od.pid.price*int(q))
                om.save()
        response={
                'status':'success',
        }
        return JsonResponse(response)     

def buy(request,uid):
        od=OrderMaster.objects.get(uid_id=uid, status='pending')
        od.status="Payment Done"
        od.save()
        response={
                'status':'success',
        }
        return JsonResponse(response)     

def history(request, uid):

        orders = OrderMaster.objects.filter(uid_id=uid, status='Payment Done').order_by('-date')
        data = []

        for om in orders:
            items = []
            item = OrderDetails.objects.filter(ordermaster=om)
            for od in item:
                items.append({
                    'pname': od.pid.pname,
                    'price': od.pid.price,
                    'quantity': od.quantity,
                    'subtotal': od.quantity * od.pid.price,
                })
            
            data.append({
                'oid': om.id,
                'status': om.status,
                'total': om.total,
                'date': om.date,
                'items': items,
            })

        response = {
                'status': 'success',
                'data': data
                }
        print('oooooooooooooo',response)
        return JsonResponse(response)



def manageproductview(request):
        data = []

        d = Products.objects.all()
        for i in d:
            data.append({
            'id': i.pk,
            'pname': i.pname,
            'des': i.description,
            'price': i.price,
            'image': i.image.name,
            })
        response={
                'status':'success',
                'data':data,
        }
        print(response)
        return JsonResponse(response)

def addproducts(request):
        product=request.POST['product']
        des=request.POST['detail']
        price=request.POST['amount']
        image_url = request.POST.get('imageUrl', '')
        p = Products(pname=product,description=des,price=price,last_updated=datetime.now(),image=image_url)
        p.save()
        response = {
        'status': 'success',
        }
        print(response)
        return JsonResponse(response)

def pedit(request, pid):
        p = Products.objects.get(id=pid)
        p.pname = request.POST['product']
        p.description = request.POST['detail']
        p.price = request.POST['amount']
        p.save()

        response = {
            'status': 'success',
            'message': 'Product updated successfully'
        }

        return JsonResponse(response)

def pdelete(request,pid):
        p = Products.objects.get(id=pid)
        p.delete()
        response={
                'status':'success'
                }
        return JsonResponse(response)

def orders(request):

        orders = OrderMaster.objects.filter(status='Payment Done').order_by('-date')
        data = []

        for om in orders:
            items = []
            item = OrderDetails.objects.filter(ordermaster=om)
            for od in item:
                items.append({
                    'pname': od.pid.pname,
                    'price': od.pid.price,
                    'quantity': od.quantity,
                    'subtotal': od.quantity * od.pid.price,
                    'image':od.pid.image.name,
                })
            
            data.append({
                'oid': om.id,
                'status': om.status,
                'total': om.total,
                'date': om.date,
                'items': items,
            })

        response = {
                'status': 'success',
                'data': data
                }
        print('oooooooooooooo',response)
        return JsonResponse(response)

