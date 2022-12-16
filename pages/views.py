from qrPage import qr
from data import *
from form import *
from qaForm import *
from getDetaliinewCV import *
from newCV import *
from downloadCV import *


from django.shortcuts import render
from django import forms
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
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from email.message import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from .data import *
import html
from django.utils.html import escape
import mimetypes
import os
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
from wsgiref.util import FileWrapper
from django.http import StreamingHttpResponse
import pdfkit as pdf

