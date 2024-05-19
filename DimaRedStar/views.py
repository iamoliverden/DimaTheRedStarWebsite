# views.py

from django.shortcuts import render
from .models import Contact


def home(request):
    with open('DimaRedStar/texts/home.txt', 'r', encoding='utf-8') as file:
        home = file.read()
    return render(request, 'DimaRedStar/home.html', {'home': home})


def bio(request):
    with open('DimaRedStar/texts/bio.txt', 'r', encoding='utf-8') as file:
        bio_text = file.read()
    return render(request, 'DimaRedStar/bio.html', {'bio_text': bio_text})



def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST.get('phone_number', '')
        message = request.POST['message']
        contact = Contact(full_name=full_name, email=email, phone_number=phone_number, message=message)
        contact.save()
    return render(request, 'DimaRedStar/contact.html')
