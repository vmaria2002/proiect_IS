from django.shortcuts import render
from EmailForm import *

# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm
from django import forms
import smtplib


  
def sendMail(request):
    
        messageSent = False
        recipient = forms.EmailField()
        message = forms.CharField(widget=forms.Textarea)
        server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("maria.vasilache02@gmail.com", "qgrqmaoreadfcszp")

        # check if form has been submitted
        if request.method == 'POST':

            form = EmailForm(request.POST)

            # check if data from the form is clean
            if form.is_valid():
                cd = form.cleaned_data
                subject = "CV-issue"
                message = cd['message']
                emm=cd['recipient']
                files = request.FILES.getlist('attach')
                #attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
            # server.sendmail("maria.vasilache02@gmail.com", ["maria.vasilache02@gmail.com", [cd['recipient']]], subject+"\n"+message) 
            # server.quit()
                files
                email = EmailMessage()

                email['Subject'] = subject
                email['From'] = emm
                email['To'] = 'maria.vasilache02@gmail.com'
                email.set_content("S-a primit o solicitare de la "+emm+"\n\n"+ "Mesajul transmis:\n "+message+"\n"+"\nATENTIE: Este posibil sa fie incarcate atasamenta!!")

                with open('D:\An3\IS\P1\cv.pdf', 'rb') as content_file:
                    
                    content = content_file.read()
                    email.add_attachment(content, maintype='application', subtype='pdf', filename='cv.pdf')

                server.send_message(email)
                

                messageSent = True

        else:
            form = EmailForm()

        return render(request, 'QR/QandA.html', {'form': form,'messageSent': messageSent})
