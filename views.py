from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

def log(request):
    return render(request,'index.html')


def first(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

def Weddings(request):
    return render(request, 'wedding.html')

def Birthday(request):
     return render(request,'birthday.html')


def contact(request):
    return render(request, 'contact.html')


def submit_form(request):
    if request.method == 'POST':
        city = request.POST.get('Destination city')


        return render(request, 'confirmation.html', {'name':city})
    else:
        return render(request, 'first.html')



