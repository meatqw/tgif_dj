from django.shortcuts import render, redirect
from .models import News, Request, User, Wallets, Question
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Routs


@login_required
def index(request):
    """INDEX (sale) page"""
    return render(request, 'main/index.html')


def entry(request):
    """ENTRY page"""
    if request.method == 'POST':

        token = request.POST['token']
        user = authenticate(request, token=token)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('entry')
    else:

        return render(request, 'main/entry.html')


@login_required
def faq(request):
    """FAQ page"""

    if request.method == 'POST':
        email = request.POST['email']
        question = request.POST['question']

        # insert data in db
        question = Question(email=email, question=question, user=request.user)
        question.save()

        return redirect('faq')

    return render(request, 'main/faq.html')


@login_required
def news(request):
    """NEWS page"""
    news = News.objects.all()
    return render(request, 'main/news.html', {'news': news})


@login_required
def news_page(request, id):
    """specific news page"""
    news = News.objects.filter(id=id).first()
    return render(request, 'main/news-page.html', {'news': news})


@login_required
def req(request):
    """REQUESTS page"""

    req = Request.objects.filter(user=request.user.id).all()
    return render(request, 'main/request.html', {'req': req})


@login_required
def wallets(request):
    """WALLETS page"""

    wallets = Wallets.objects.filter(user=request.user.id).all()
    return render(request, 'main/wallets.html', {'wallets': wallets})


@login_required
def logout_(request):
    """Logout"""
    logout(request)
    return redirect('entry')
