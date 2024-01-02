from django.shortcuts import render

# Create your views here.

def home(request):
    s=''
    if request.method == 'POST':
        n1=eval(request.POST.get('num1'))
        n2=eval(request.POST.get('num2'))
        op=request.POST.get('op')
        
        if op == '+':
            s=n1+n2
        if op == '-':
            s=n1-n2
        if op == '*':
            s=n1*n2
        if op == '/':
            s=n1/n2
        
    return render(request,"index.html",{"s" : s})
