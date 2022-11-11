from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('switchStatus', views.switch_req_status, name='switchStatus'),
    path('switchPower', views.switch_power, name='switchPower'),
    path('entry', views.entry, name='entry'),
    # path('entry', include('django.contrib.auth.urls')),
    path('faq', views.faq, name='faq'),
    path('news', views.news, name='news'),
    path('news/<int:id>', views.news_page, name='news_page'),
    path('req', views.req, name='req'),
    path('wallets', views.wallets,  name='wallets'),
    path('wallets/<int:id>', views.del_wallet,  name='delWallets'),
    path('updateWallet', views.update_wallets,  name='updateWallet'),
    path('switchWalletStatus', views.switch_wallet_status, name='switchWalletStatus'),
    path('accounts/login', views.index, name='login'),
    path('getWallets', views.get_wallets, name='getWallets'),
    path('logout', views.logout_, name='logout')

] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
