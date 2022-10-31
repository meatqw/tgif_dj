from django.shortcuts import render, redirect
from .models import News, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Routs
@login_required
def index(request):
    return render(request, 'main/index.html')

def entry(request):
    if request.method == 'POST':

        token = request.POST['token']
        user = authenticate(request, token=token)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('entry')
    else:

        return render(request, 'main/entry.html')

@login_required
def faq(request):
    return render(request, 'main/faq.html')

@login_required
def news(request):
    news = News.objects.all()
    return render(request, 'main/news.html', {'news': news})

@login_required
def news_page(request, id):
    news = News.objects.filter(id=id).first()
    return render(request, 'main/news-page.html', {'news': news})

@login_required
def request(request):
    return render(request, 'main/request.html')

@login_required
def wallets(request):
    return render(request, 'main/wallets.html')

@login_required
def logout_(request):
    logout(request)
    return redirect('entry')