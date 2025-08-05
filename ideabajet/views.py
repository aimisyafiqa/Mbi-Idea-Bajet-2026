from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Admin, Elemen1, Lokasi, Elemen2, Elemen3, Elemen4
# Create your views here.

def login(request):
    if request.method == 'POST':
        adminid = request.POST.get('id')
        password = request.POST.get('password')

        try:
            admin = Admin.objects.get(adminid=adminid, password=password)
            request.session['id'] = admin.adminid  # simpan dalam session
            messages.success(request, "Succesfully Login.", extra_tags='admin')
            return render(request,'dashboard.html', {'message': 'Sucessfully Login'})  # ganti dengan nama URL dashboard admin awak
        except Admin.DoesNotExist:
            return render(request, 'login.html', {'message': 'Invalid Admin ID or Password',})
    return render (request,"login.html")

def dashboard(request):
    return render(request,"dashboard.html")

def lokasi(request):
    if request.method == 'POST':
        listloc = request.POST.get('list_lokasi')
        if listloc:
            Lokasi.objects.create(list_lokasi=listloc)
            return redirect('lokasi')
    data = Lokasi.objects.all()
    return render(request, 'lokasi.html', {'data': data})

def delete_lokasi(request, lid):
    Lokasi.objects.filter(lid=lid).delete()
    return redirect('lokasi')

def e1(request):
    if request.method == 'POST':
        liste1 = request.POST.get('e1')
        if liste1:
            Elemen1.objects.create(e1=liste1)
            return redirect('e1')
    data = Elemen1.objects.all()
    return render(request, 'e1.html', {'data': data})

def delete_e1(request, e1id):
    Elemen1.objects.filter(e1id=e1id).delete()
    return redirect('e1')

def e2(request):
    if request.method == 'POST':
        liste2 = request.POST.get('e2')
        if liste2:
            Elemen2.objects.create(e2=liste2)
            return redirect('e2')
    data = Elemen2.objects.all()
    return render(request, 'e2.html', {'data': data})

def delete_e2(request, e2id):
    Elemen2.objects.filter(e2id=e2id).delete()
    return redirect('e2')

def e3(request):
    if request.method == 'POST':
        liste3 = request.POST.get('e3')
        if liste3:
            Elemen3.objects.create(e3=liste3)
            return redirect('e3')
    data = Elemen3.objects.all()
    return render(request, 'e3.html', {'data': data})

def delete_e3(request, e3id):
    Elemen3.objects.filter(e3id=e3id).delete()
    return redirect('e3')

def e4(request):
    if request.method == 'POST':
        liste4 = request.POST.get('e4')
        if liste4:
            Elemen4.objects.create(e4=liste4)
            return redirect('e4')
    data = Elemen4.objects.all()
    return render(request, 'e4.html', {'data': data})

def delete_e4(request, e4id):
    Elemen4.objects.filter(e4id=e4id).delete()
    return redirect('e4')

