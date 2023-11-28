from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def art_works(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def account(request):
    return render(request, 'account.html')
