from django.shortcuts import render,HttpResponse

def Home(request) : 
    context  = {
        'variable1':  'Prakhar Saxena' ,
        'variable2':  'SRM institute of Science and Technology'
    }
    return render(request , 'Homepage.html' , context)

