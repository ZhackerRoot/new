from django.shortcuts import render, redirect
from .forms import LoginForm

def index(request):
    X = LoginForm()
    if request.method == 'POST':
       x = LoginForm(request.POST)
       if x.is_valid():
           try:
               return redirect('/')
           except:
               pass
    else:
        X = LoginForm()
    return render(request, 'index.html', {'forms': X})

def home(request):
    context = {
        'Login': ['Apple', 'Banana'],
        'Register': ['Ahmad', 'Rustam'],
        'LogOut': ['Mila', 'Bonu',]
    }
    return render(request, 'home.html', {'xs': context})