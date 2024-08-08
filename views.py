from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django keen  infotech !</h2>")
def index(request):
    return render(request,'index.html')
def about(request):
    return  render(request,'about.html')
def Register(request):
    return  render(request,'Register.html')
def checkout(request):
    return render(request, 'checkout.html');
def contact(request):
    return render(request, 'contact.html');
def Shopnow(request):
    return render(request, 'Shopnow.html');
def login(request):
    return  render(request,'login.html');
def detail(request):
    return render(request,'detail.html');
def header(request):
    return  render(request,'header.html')
def footer(request):
    return  render(request,'footer.html')

def content(request):
    return  render(request,'content.html')
def menu(request):
    return  render(request,'menu.html')
def about(request):
    return  render(request,'about.html')
def dresses(request):
    return  render(request,'dresses.html')
def cart(request):
    return  render(request,'cart.html')


