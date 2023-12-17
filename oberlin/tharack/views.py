from django.shortcuts import render
# Create your views here.

import segno

def home(request):
    return render(request,"tharack/home.html")
def about(request):
    return render(request,"tharack/about.html")
def contact(request):
    return render(request,"tharack/contact.html")

def portfolio(request):
    return render(request,"tharack/portfolio.html")
def generate(request):
    code = segno.make_qr('Burundi')
    image = code.save("tharack/files/images/image.png",scale = 5)
    print(image)
    return render(request,"tharack/resume.html",{
        'image':image
    })
    
