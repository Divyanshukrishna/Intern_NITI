from django.shortcuts import render
from page.models import info

# Create your views here.

def google(request):
    return render(request,"google.html")


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        data = info(name=name, email=email, lname=lname , phone=phone , password=password)
        data.save()

    return render(request,"index.html")




