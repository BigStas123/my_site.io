from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'main/index.html')
def theme1(request):
    return render(request,'main/theme1.html')
def theme2(request):
    return render(request,'main/theme2.html')
def theme3(request):
    return render(request,'main/theme3.html')
def theme4(request):
    return render(request,'main/theme4.html')
def theme5(request):
    return render(request,'main/theme5.html')