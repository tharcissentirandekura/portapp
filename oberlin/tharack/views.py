from django.shortcuts import render,redirect
import segno
from .models import qrcode

def home(request):
    return render(request,"tharack/home.html")
def about(request):
    return render(request,"tharack/about.html")
def contact(request):
    return render(request,"tharack/contact.html")

def portfolio(request):
    return render(request,"tharack/portfolio.html")
def resume(request):
    if request.method == 'POST':
        data = request.POST['data']

        # Generate QR code
        qr = segno.make(data)

        # Save QR code image to model
        code = qrcode(data=data)
        qr.save(code.image.path, kind='png')
        code.save()
        print(code)
        # Redirect to QR code detail page
        return redirect('qrcode_detail', pk=code.pk)

    return render(request, 'tharack/resume.html')

    
    
