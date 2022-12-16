#metoda pentru observer:)

from django import forms
import smtplib
from form import *
from django.shortcuts import render

from observer import *


def qaa(request): 
    subject = Observer.ConcretSendMail()
    observer_a = Observer.ConcreteObserver()
    subject.send(observer_a)
    subject.some_business_logic() #notify
