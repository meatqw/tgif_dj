from django.shortcuts import render, redirect
from .models import News, Request, User, Wallets, Question, Faq, Tg, MainInfo, Status
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .bot import send_msg

# Routs

# ---------- PAGE RENDER -----------


@login_required
def index(request):
    """INDEX (sale) page"""

    req = Request.objects.filter(user=request.user.id).all()
    in_active = [i for i in req if str(i.status) == 'Активная']
    closed = [i for i in req if str(i.status) == 'Завершенная']
    in_check = [i for i in req if str(i.status) == 'На проверке']
    all = [i for i in req if str(i.status) != 'Новая']

    return render(request, 'main/index.html', {'in_active': in_active, 'closed': closed, 'in_check': in_check, 'all': all,
     'escrow': ger_escrow(request.user.id), 'main': MainInfo.objects.all()[0]})


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

        return render(request, 'main/entry.html', {'escrow': ger_escrow(request.user.id)})


@login_required
def faq(request):
    """FAQ page"""
    faq = Faq.objects.all()

    if request.method == 'POST':
        email = request.POST['email']
        question = request.POST['question']

        # insert data in db
        question = Question(email=email, question=question, user=request.user)
        question.save()

        return redirect('faq')

    return render(request, 'main/faq.html', {'faq': faq, 'escrow': ger_escrow(request.user.id), 'main': MainInfo.objects.all()[0]})


@login_required
def news(request):
    """NEWS page"""
    news = News.objects.all()
    return render(request, 'main/news.html', {'news': news, 'escrow': ger_escrow(request.user.id), 'main': MainInfo.objects.all()[0]})


@login_required
def news_page(request, id):
    """specific news page"""
    news = News.objects.filter(id=id).first()
    return render(request, 'main/news-page.html', {'news': news, 'escrow': ger_escrow(request.user.id), 'main': MainInfo.objects.all()[0]})


@login_required
def req(request):
    """REQUESTS page"""
    status_new = Status.objects.filter(status_name='Новая').first()
    if request.method == 'POST':
        status = Status.objects.filter(status_name='Активная').first()
        print(status)
        wallets = request.POST['wallets']
        user = request.user
        status = status.id
        id = request.POST['id']
        Request.objects.filter(id=id).update(
            user=user, status=status, wallets=wallets)

        return redirect('req')

    req = Request.objects.filter(user=request.user, status=status_new.id).all()
    return render(request, 'main/request.html', {'req': req, 'escrow': ger_escrow(request.user.id), 'main': MainInfo.objects.all()[0]})


@login_required
def wallets(request):
    """WALLETS page"""

    wallets = Wallets.objects.filter(user=request.user.id).all()
    return render(request, 'main/wallets.html', {'wallets': wallets, 'escrow': ger_escrow(request.user.id), 'main': MainInfo.objects.all()[0]})


# --------------------------------

def ger_escrow(user):
    req = Request.objects.filter(user=user).all()
    escrow = sum([int(i.amount) for i in req if str(i.status) == 'Активная'])

    return escrow


@login_required
def switch_power(request):
    """SWITCH power status"""

    if request.method == 'POST':
        status = request.POST['status']
        
        if status == 'true':
            send_tg(Tg.objects.all(), f'Пользователь {request.user.token} Готов к работе 👍')
            
            status = True
        else:
            status = False

        User.objects.filter(id=request.user.id).update(power=status)

        return JsonResponse({'status': status})


@login_required
def switch_req_status(request):
    """SWITCH_REQ_STATUS"""

    if request.method == 'POST':

        status = request.POST['status']
        id = request.POST['id']
        
        if status != 'del':
            status = Status.objects.filter(status_name=request.POST['status']).first()
            
            User.objects.filter(id=request.user.id).update(
                requests=request.user.requests + 1)
            Request.objects.filter(id=id).update(status=status)

            send_tg(Tg.objects.all(), f'Пользователь {request.user.token}\nИзменил статус заявки {id} ✅')
            
            return redirect('index')

        else:
            Request.objects.filter(id=id).delete()

        return JsonResponse({'status': status})


@login_required
def get_wallets(request):

    if request.method == 'POST':
        props = request.POST['props']

        wallet = Wallets(props=props, user=request.user, status=True)
        wallet.save()

    else:

        wallets = Wallets.objects.filter(
            user=request.user.id, status=True).all()
        wallets_json = [{'id': i.id, 'props': i.props,
                         'status': i.status} for i in wallets]
        return JsonResponse({'wallets': wallets_json})


@login_required
def del_wallet(request, id):
    """WALLETS del"""
    wallets = Wallets.objects.filter(user=request.user.id).all()
    Wallets.objects.filter(id=id).delete()
    return render(request, 'main/wallets.html', {'wallets': wallets, 'escrow': ger_escrow(request.user.id)})


@login_required
def switch_wallet_status(request):
    """wallet_status"""

    if request.method == 'POST':
        status = request.POST['status']
        id = request.POST['id']

        if status == 'true':
            status = True
        else:
            status = False

        Wallets.objects.filter(id=id).update(status=status)

    return redirect('wallets')


@login_required
def logout_(request):
    """Logout"""
    logout(request)
    return redirect('entry')

@login_required
def update_wallets(request):

    if request.method == 'POST':
        props = request.POST['props']
        id = request.POST['id']

        Wallets.objects.filter(id=id).update(props=props)

    return redirect('wallets')


def send_tg(ids, text):

    for id in ids:
        send_msg(id.tg_id, text)

