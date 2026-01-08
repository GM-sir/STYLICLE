from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def contactus(request):
    return render(request, 'contactus.html')
def sign_up(request):
    return render(request, 'auth/sign_up.html')
def user_login(request):
    return render(request, 'auth/user_login.html')
