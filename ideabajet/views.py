from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin 
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
            return render(request, 'login.html', {'message': 'Invalid ID or IC number',})
    return render (request,"login.html")

def dashboard(request):
    return render(request,"dashboard.html")

