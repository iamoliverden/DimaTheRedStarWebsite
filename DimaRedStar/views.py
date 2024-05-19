# views.py

from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, 'DimaRedStar/index.html')

def bio(request):
    return render(request, 'DimaRedStar/bio.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contact = Contact(name=name, email=email)
        contact.save()
    return render(request, 'DimaRedStar/contact.html')
