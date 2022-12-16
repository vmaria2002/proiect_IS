from __future__ import annotations
from Observer import Observer, abstractmethod
from random import randrange
from typing import List
from django import forms
from django.shortcuts import render
from django.core import mail
import smtplib
from django.core.mail import BadHeaderError, send_mail
from django.core.mail import EmailMessage
from email.message import EmailMessage
import Observer
from form import *
from qaForm import *  #pt a prelua toate mesajele


#Clasa abstracta care determina trimiterea unei modificari
class SendEmail(Observer):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        Genereaza trimiterea
        """
        pass

email = EmailMessage()
#Clasa concreta:
class ConcretSendMail(SendEmail):
    """
    Cei care vor primi email 
    """
    _observers: List[Observer] = qaa.__get__(__name__) #luam numele obtinut 
    #cand atasam trimitem mail
    def send(self, observer: Observer, email, request) -> None:
        if request.method == 'POST':
                form = EmailForm(request.POST)
                cd = form.cleaned_data
                subject = "CV-issue"
                message = cd['message']
                emm=cd['recipient']
                files = request.FILES.getlist('attach')


           

        email['Subject'] = subject
        email['From'] = emm
        email['To'] = 'maria.vasilache02@gmail.com'
        email.set_content("S-a primit o solicitare de la "+emm+"\n\n"+ "Mesajul transmis:\n "+message+"\n"+"\nATENTIE: Este posibil sa fie incarcate atasamenta!!")

        with open('D:\An3\IS\P1\cv.pdf', 'rb') as content_file:
                
                content = content_file.read()
                email.add_attachment(content, maintype='application', subtype='pdf', filename='cv.pdf')
        self._observers.append(observer)


    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        #metoda care declanseaza notificarea atunci cand este apelata...
        print("\nSend email")
        self.notify()


class Observer(EmailMessage):
    """
    Observatorul va face modificari, el va avea rol de a face update
    """

    @abstractmethod
    def update(self, subject: EmailMessage) -> None:
        pass


"""
Observer-ul se updateaza
"""

class ConcreteObserver(Observer):
    def update(self, EmailMessage, request) -> None:
            server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("maria.vasilache02@gmail.com", "qgrqmaoreadfcszp")
            server.send_message(email)
            messageSent = True

            return render(request, 'QR/QandA.html', {'form': form, 'messageSent': messageSent, })
