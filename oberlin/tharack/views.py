from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,"tharack/home.html")
def about(request):
    return render(request,"tharack/about.html")
def contact(request):
    return render(request,"tharack/contact.html")

def portfolio(request):
    return render(request,"tharack/portfolio.html")
