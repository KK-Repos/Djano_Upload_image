from django.shortcuts import render

from django.conf import settings
from .models import Upload
# Create your views here.
def index(request):

    pic = Upload.objects.all()

    return render(request,'index.html',{'pic':pic,'media_url':settings.MEDIA_URL})