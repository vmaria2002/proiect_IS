from django.shortcuts import render

# Create your views here.
# pages/views.py
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
import qrcode
import qrcode.image.svg
from io import BytesIO
from django.core import mail
from django.core.mail import send_mail
from django.core import mail
import smtplib
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

send_mail(
    subject = 'Test Mail',
    message = 'Maria V',
    from_email = 'maria.vasilache02@gmail.com',
    recipient_list = ['maria.vasilache02@gmail.com',],
    fail_silently = False,
)

 


class HomePageView(TemplateView):
    template_name = 'home.html'

def newCV(request):
    return render(request, 'QR/newCV.html')  

def myCv(request):
     return render(request, 'QR/MyCV.html')  

def qr(request):
     return render(request, 'QR/QRcode.html')  

def qaa(request): 
     server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
     server.login("maria.vasilache02@gmail.com", "qgrqmaoreadfcszp")
     server.sendmail("maria.vasilache02@gmail.com", "maria.vasilache02@gmail.com", "perfect")
     server.quit()
#afiseaza doar in consola     
#     subject = request.POST.get('subject', 'hhh')
#     message = request.POST.get('message', 'jjj')
#     from_email = request.POST.get('from_email', 'maria.vasilache02@gmail.com')
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['maria.vasilache02@gmail.com'])
#         except BadHeaderError:
     #return HttpResponse('ok')
     return render(request, 'QR/QandA.html')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')



def qr(request):
     context = {}
     if request.method == "POST":
          factory = qrcode.image.svg.SvgImage
          img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20)
          stream = BytesIO()
          img.save(stream)
          context["svg"] = stream.getvalue().decode()

     return render(request, "QR/QRcode.html", context=context)

