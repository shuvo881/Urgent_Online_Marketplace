from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from items.models import Category, Item
from .forms import SignupFrom, LoginForm
from django.urls import reverse


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html',
                  {
                      'categories': categories,
                      'items': items,
                  })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Completed')
            return redirect(reverse('login'))
        else:
            messages.error(request, "")

    else:
        form = SignupFrom()
    return render(request, 'core/signup.html', {'form': form})


def signin(request):
    print("no")
    if request.method == 'POST':
        print('yes')
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request=request, username=username, password=password)
            print("user:", user)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful, enjoy the website")
                return redirect('index')
            else:
                messages.error(request, "Username or password is invalid")
        except Exception as e:
            messages.error(request, e)
    else:
        form = LoginForm()
    return render(request, 'core/signin.html', {'form': form})


def signout(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect(reverse('signin'))
