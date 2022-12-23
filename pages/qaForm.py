#metoda pentru observer:)

from django import forms
from email.message import EmailMessage
import smtplib
from form import *
from django.shortcuts import render

from observer import *

def observer(request):
    obj1 = Observer('Email 1')
    view1 = UpdateEmail()
    #atasez observator
    obj1.attach(view1)
    #modific email (s-a completat formularul)
    obj1.data = newValue() #noul email, prin notify(), apelez functia de send mail, pentru ce s-a generat 

#preiau datele din interfata
def newValue(request):
 if request.method == 'POST':
        form = EmailForm(request.POST)
        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            message = cd['message']
            emm=cd['recipient']
            return message+' '+ 'maria.vasilache02@gmail.com'+' '+ emm 
