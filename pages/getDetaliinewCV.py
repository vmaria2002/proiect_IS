from .data import *
import html

def country(nr):
    rez=""
    if nr=="1":
        rez="Romania/Cluj-Napoca"
    elif nr=="2":
        rez="Romania/Iasi"
    else:
        rez="France/Paris"

    return rez

socialContact = [
        'fab fa-github',
        'fab fa-linkedin',
        'fab fa-facebook',
    ]

def getSocials(shema, link):
    i = 0
    gotoshow = ""
    while i < len(shema):
        if link[i]:
            skill = "<a class='social' target='_blank' href='" + link[i] + "'><i class='" + shema[i] + "'></i></a>"
            gotoshow = gotoshow + skill
        else:
            gotoshow = gotoshow
        i += 1
        if i == len(shema):
            return html.unescape(gotoshow)

def getSkills(yourSkills):
    rez=yourSkills.split(", ")
    i = 0
    gotoshow = ""
    while i < len(rez):
        skill = "<li><span class='main full'>" + rez[i] + "</span></li>"
        i += 1
        gotoshow = gotoshow + skill
        if i == len(rez):
            return html.unescape(gotoshow)


def getListWithYear(shema, year):
    i = 0
    gotoshow = ""
    skill = "<li><span class='main'>" + shema + "</span><span class='year'>" + year + "</span></li>"
    gotoshow = gotoshow + skill

    return html.unescape(gotoshow)

def getListWithLink(shema, link):
    i = 0
    gotoshow = ""
    skill = "<li><a target='_blank' href='" + link + "'>" + shema + "</a></li>"
    gotoshow = gotoshow + skill
    return html.unescape(gotoshow)


def getLists(shema):
    i = 0
    gotoshow = ""
    while i < len(shema):
        skill = "<li>" + shema[i] + "</li>"
        i += 1
        gotoshow = gotoshow + skill
        if i == len(shema):
            return html.unescape(gotoshow)
def getSocial(shema, link):
    i = 0
    gotoshow = ""
    while i < len(shema):
        if link[i]:
            skill = "<a class='social' target='_blank' href='" + link[i] + "'><i class='" + shema[i] + "'></i></a>"
            gotoshow = gotoshow + skill
        else:
            gotoshow = gotoshow
        i += 1
        if i == len(shema):
            return html.unescape(gotoshow)  
def getListWithYea(shema, year):
    i = 0
    gotoshow = ""
    while i < len(shema):
        if year[i]:
           skill = "<li><span class='main'>" + shema[i] + "</span><span class='year'>" + year[i] + "</span></li>"
        else:
           skill = "<li><span class='main full'>" + shema[i] + "</span></li>"
        i += 1
        gotoshow = gotoshow + skill
        if i == len(shema):
            return html.unescape(gotoshow)  
def getListWithLin(shema, link):
    i = 0
    gotoshow = ""
    while i < len(shema):
        if link[i]:
            skill = "<li><a target='_blank' href='" + link[i] + "'>" + shema[i] + "</a></li>"
        else:
            skill = "<li><a target='_blank'>" + shema[i] + "</a></li>"
        i += 1
        gotoshow = gotoshow + skill
        if i == len(shema):
            return html.unescape(gotoshow)

val= {
        'titleCV' : titleCV,
        'yourName' : yourName,
        'yourProfession' : yourProfession,
        'yourBio' : yourBio,
        'yourCountry' : yourCountry,
         'yourContact' : getSocial(socialContact, yourContact),
        'yourBirthday' : yourBirthday,
         'yourHobbies' : getLists(yourHobbies),
         'yourCerts' : getLists(yourCerts),
         'yourEdu' : getListWithYea(yourEdu, eduYear),
         'yourWork' : getListWithYea(yourWork, workYear),
         'yourProject' : getListWithLin(yourProject, projectLink),
         'yourExtras': getLists(yourExtras),
        'footerText': footerText
        }

def data():
    #sa le preia din baza de date
    val['yourName']="Ana"
    rez= {
        'titleCV' : titleCV,
        'yourName' : yourName,
        'yourProfession' : yourProfession,
        'yourBio' : yourBio,
        'yourCountry' : yourCountry,
         'yourContact' : getSocial(socialContact, yourContact),
        'yourBirthday' : yourBirthday,
         'yourHobbies' : getLists(yourHobbies),
         'yourCerts' : getLists(yourCerts),
         'yourEdu' : getListWithYea(yourEdu, eduYear),
         'yourWork' : getListWithYea(yourWork, workYear),
         'yourProject' : getListWithLin(yourProject, projectLink),
         'yourExtras': getLists(yourExtras),
        'footerText': footerText
        }
    return rez