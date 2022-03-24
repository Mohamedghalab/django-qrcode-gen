from django.shortcuts import render, redirect
from .models import QrCodeGen
from .forms import QrCodeForm

def home(request):
    qr_code = QrCodeGen.objects.all()
    if request.method == "POST":
        form = QrCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=QrCodeForm()
    return render(request, 'home.html', {'form':form, 'qrcode':qr_code})
