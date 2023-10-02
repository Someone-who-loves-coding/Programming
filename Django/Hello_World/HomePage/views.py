from django.shortcuts import render,HttpResponse
from HomePage.models import Contact
from datetime import datetime

def Home(request) : 
    if request.method == "POST" :
        name = request.POST.get('name')
        Email = request.POST.get('email')
        comment = request.POST.get('comment')
        contact =  Contact( name=name , Email=Email , Comment=comment , Date=datetime.today())
        contact.save()
    return render(request , 'Index.html')