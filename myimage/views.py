from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
import os
from PIL import Image
basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_photo(request):
    f1 = request.FILES['pic']
    img = Image.open(f1)
    img.save('current_photo.jpg')
    return HttpResponse('i get it')

def show_photo(request):
    os.system('cp /home/pi/current.jpg /home/pi/pi_image/static/current_photo.jpg')
    return render(request,'show_image.html',{})
