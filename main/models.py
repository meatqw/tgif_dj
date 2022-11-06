from django.db import models
from django.contrib import admin
# news db model


class News(models.Model):
    '''News model'''
    title = models.CharField('Title', max_length=50)
    img = models.ImageField(null=True, blank=True, upload_to='images/')
    description = models.TextField('Description')
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class User(models.Model):
    '''User model'''
    token = models.CharField('Token', max_length=50)
    requests = models.IntegerField('Requests')
    escrow = models.IntegerField('escrow')
    balance = models.IntegerField('balance')
    received = models.IntegerField('received')
    date_joined = models.DateTimeField(
        'data joined', auto_now_add=True, blank=True)
    last_login = models.DateTimeField(
        'last login', auto_now_add=True, blank=True)
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
    props = models.CharField('Props', max_length=50)
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
    status_name = models.CharField('status', max_length=50)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.status_name
    

class Request(models.Model):
    '''Request model'''
    amount = models.CharField('amount', max_length=50)
    lifespan = models.IntegerField('lifespan')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=False)
    condition = models.BooleanField('condition', default=False)
    wallets = models.JSONField('Wallets', default='{}')
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    

    def __str__(self):
        return self.amount
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Question(models.Model):
    '''Question model'''
    email = models.CharField('email', max_length=100)
    question = models.TextField('question')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class RequestAdmin(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Request._meta.fields]

class WalletsAdmin(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Wallets._meta.fields]

class UserAdmin(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in User._meta.fields]

class NewsAdmin(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in News._meta.fields]

class QuestionAdmin(admin.ModelAdmin):
    '''Show all fields in admin'''
    list_display = [field.name for field in Question._meta.fields]