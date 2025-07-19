from django.shortcuts import render
#usa-se esta página quando meu debug está em False

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')