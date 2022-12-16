from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import os

def downloadFile(request):   

     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     filename='CV.mhtml'
     thefile= base_dir + '/Files/'+ filename
     filename = os.path.basename(thefile)
     chunk_size =8192
     reponse = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'), chunk_size), content_type =mimetypes.guess_type(thefile)[0])
     reponse['Content-Length']=os.path.getsize(thefile)
     reponse['Content-Disposition']="Attachment;filename=%s" % filename
     return reponse
