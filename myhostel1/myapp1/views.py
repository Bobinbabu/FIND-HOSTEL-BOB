from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import uregister
from .models import ulogin
from .models import hregister
from .models import hlogin
from django.contrib import messages

def display(request):
    return render(request, 'index.html')

def userreg(request):
    return render(request, 'user registration.html')

def usignin(request):
    return render(request, 'usignin.html')

def hostelreg(request):
    return render(request, 'hostel registration.html')

def hsignin(request):
    return render(request, 'hsignin.html')

def uandhreg(request):
    return render(request, 'u and h reg.html')

def uregistered(request):
    if request.method == "POST":
        u = request.POST['u1']
        e = request.POST['e1']
        p = request.POST['p1']
        data = uregister.objects.create(username=u, email=e)
        data.save()
        data1 = ulogin.objects.create(username=u, password=p)
        data1.save()
        return redirect('/usignin')


def ulogged(request):
    abc={}
    if request.method == 'POST':
        u = (request.POST['u1'])
        p = int(request.POST['p1'])
        try:
            data = ulogin.objects.get(username=u)
            if data.password == p:
                request.session['id'] = u
                return redirect(uprofile)
            else:
                abc['key'] = 'password incorrect'
                return render(request,'usignin.html',abc)
        except Exception:
            abc['key'] = 'username incorrect'
            return render(request,'usignin.html',abc)


def uprofile(request):
    if 'id' in request.session:
        x = request.session['id']
        y = uregister.objects.filter(username=x)
        return render(request, 'uprofile.html', {"data": y})
    else:
        return redirect(uprofile)


def ulogout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(display)

def hregistered(request):
    if request.method == "POST":
        u = request.POST['u1']
        e = request.POST['e1']
        p = request.POST['p1']
        data = hregister.objects.create(username=u, email=e)
        data.save()
        data1 = hlogin.objects.create(username=u, password=p)
        data1.save()
        return HttpResponse("created")


def hlogged(request):
    if request.method == 'POST':
        u = (request.POST['u1'])
        p = int(request.POST['p1'])
        try:
            data = hlogin.objects.get(username=u)
            if data.password == p:
                request.session['id1'] = u
                return redirect(hprofile)
            else:
                return HttpResponse('password incorrect')
        except Exception:
            return HttpResponse('username incorrect')


def hprofile(request):
    if 'id1' in request.session:
        x = request.session['id1']
        y = hregister.objects.filter(username=x)
        return render(request, 'hprofile.html', {"data": y})
    else:
        return redirect(hprofile)


def hlogout(request):
    if 'id1' in request.session:
        request.session.flush()
        return redirect(display)

