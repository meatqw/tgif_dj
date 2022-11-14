from django.db import models
from django.contrib import admin
# news db model


class News(models.Model):
    '''News model'''
    title = models.CharField('Название', max_length=50)
    img = models.ImageField(null=True, blank=True, upload_to='images/')
    description = models.TextField('Текст')
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class User(models.Model):
    '''User model'''
    token = models.CharField('Токен', max_length=50)
    power = models.BooleanField(default=False)
    requests = models.IntegerField('Заявки')
    escrow = models.IntegerField('Эскроу')
    balance = models.IntegerField('Баланс')
    received = models.IntegerField('Получено')
    date_joined = models.DateTimeField(
        'Дата создания', auto_now_add=True, blank=True)
    last_login = models.DateTimeField(
        'Последний визит', auto_now_add=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.token

    def is_authenticated(self, request):
        return True

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, app_label):
        return False

    def get_username(self):
        return self.token

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Wallets(models.Model):
    '''Wallets model'''
    props = models.CharField('Реквизиты', max_length=50)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.props
    
    class Meta:
        verbose_name = 'Кошелёк'
        verbose_name_plural = 'Кошельки'
        
class Status(models.Model):
    '''status for requests'''
    status_name = models.CharField('Наименование статуса', max_length=50)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.status_name
    
    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявок'
    

class Request(models.Model):
    '''Request model'''
    amount = models.CharField('Сумма', max_length=50)
    send = models.CharField('Отправляем', max_length=50)
    get = models.CharField('Получаем', max_length=50)
    deals = models.CharField('Сделки', max_length=50)
    lifespan = models.IntegerField('Срок жизни')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=False, default="Новая")
    # condition = models.BooleanField('condition', default=False)
    wallets = models.JSONField('Реквизиты', default='{}')
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    

    def __str__(self):
        return self.amount
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Question(models.Model):
    '''Question model'''
    email = models.CharField('Почта', max_length=100)
    question = models.TextField('Вопрос')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Faq(models.Model):
    '''Faq model'''
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст')
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'


class Tg(models.Model):
    '''Faq model'''
    tg_id = models.CharField('TG id', max_length=200)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.tg_id
    
    class Meta:
        verbose_name = 'TG ID'
        verbose_name_plural = 'TG IDs'

class MainInfo(models.Model):
    '''MainInfo model'''
    account_number = models.CharField('Номер счета', max_length=200)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.account_number
    
    class Meta:
        verbose_name = 'Номер счета'
        verbose_name_plural = 'Номер счета'


class RequestAdmin(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Request._meta.fields]

class MainInfoAdmin(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in MainInfo._meta.fields]

class FaqAdmin(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Faq._meta.fields]

class WalletsAdmin(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Wallets._meta.fields]

class UserAdmin(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in User._meta.fields if field.name not in ['is_admin', 'is_active', 'is_staff', 'is_superuser']]

class NewsAdmin(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in News._meta.fields]

class QuestionAdmin(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Question._meta.fields]