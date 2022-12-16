from django.shortcuts import render

def newCV(request):
    return render(request, 'QR/newCV.html')  