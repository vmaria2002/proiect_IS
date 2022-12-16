
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from getDetaliinewCV import *

def index(request):
      return render(request, 'index.html')
def validate(request):
   if request.method == 'POST':
      prenume= request.POST['prenume']
      nume=request.POST['nume']
      attach= "/static/img/"+request.POST['attach']
      
      profession=request.POST['profession']
      yourBio=request.POST['yourBio']
      yourCountry=country(request.POST['yourCountry'])

      yourBirthday=request.POST['yourBirthday']


      git=request.POST['gitHub']
      linkedin= request.POST['linkedin']      
      facebook=request.POST['facebook']  
      yourContac = [git, linkedin, facebook]
    

      yourContact = getSocials(socialContact, yourContac)

      yourSkill =request.POST['yourSkills']  
      yourSkills =getSkills(yourSkill)

      yourHobbie =request.POST['yourHobbies']  
      yourHobbie =getSkills(yourHobbie)

      eduYear=request.POST['eduYear']  
      yourEdus=request.POST['yourEdu']   
      yourEdu = getListWithYear(yourEdus, eduYear)

      work=request.POST['work']  
      year_work=request.POST['year_work']  

      yourWork=getListWithYear(work, year_work)

      yourProjects=request.POST['yourProject']
      projectLink=request.POST['projectLink']  
       
      yourProject=getListWithLink(yourProjects, projectLink)

      val['yourName']=prenume+" "+nume
      val['profession']=profession
      val['yourBio']=yourBio
      val['attach']=attach
      val['yourCountry']=yourCountry
      val['yourBirthday']=yourBirthday 
      val['socialContact']=socialContact
      val['yourContact']= yourContact
      val['yourSkills']=yourSkills
      val['yourHobbies']=yourHobbie
      val['yourEdu']=yourEdu
      val['yourWork']=yourWork
      val['yourProject']=yourProject  

      dict = {
         'prenume': prenume+" "+nume,
         'profession':profession,
          'yourBio':yourBio,
          'attach':attach,
          'yourCountry':yourCountry,
          'yourBirthday':yourBirthday,
          'socialContact':socialContact,
          'yourContact': yourContact,
          'yourSkills':yourSkills,
          'yourHobbies':yourHobbie,
          'yourEdu':yourEdu,
           'yourWork':yourWork,
           'yourProject' :yourProject

        #  'password': password,
        
      }
     
      return render(request, 'validate.html', dict)   



def pdf_report_create(request):

    dict = val
       
    template_path = 'pdfReport.html'

    context =dict

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="cv_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

# create a pdf
    pisa_status = pisa.CreatePDF(  html, dest=response)
# if error then show some funy view
    if pisa_status.err:
     return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response 