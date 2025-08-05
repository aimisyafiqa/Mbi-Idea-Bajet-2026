from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Admin, Elemen1, Lokasi
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