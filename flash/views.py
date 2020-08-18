from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserDetails
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    users=UserDetails.objects.all()
    return render(request,'elements.html',{'title':'Elements','users':users})
def newuser(request):
    return render(request,'newelement.html',{'title':'New Element'})
def details(request):
    user=UserDetails()
    print(request.FILES)
    if request.method=='POST' and request.FILES['imagesu']:
        user.name=request.POST['name']
        user.city=request.POST['city']
        user.category=request.POST['category']
        user.ref=request.POST['ref']
        user.desc=request.POST['desc']
        img=request.FILES['imagesu']
        fs=FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)
        user.img=uploaded_file_url
        user.save()
    return redirect('index')