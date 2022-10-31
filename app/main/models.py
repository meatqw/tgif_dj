from django.db import models

# news db model
class News(models.Model):
    title = models.CharField('Title', max_length=50)
    img = models.ImageField(null=True, blank=True, upload_to='images/')
    description = models.TextField('Description')
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


# user db model
class User(models.Model):
    token = models.CharField('Token', max_length=50)
    requests =  models.IntegerField('Requests')
    escrow = models.IntegerField('escrow')
    balance = models.IntegerField('balance')
    received = models.IntegerField('received')
    date_joined = models.DateTimeField('data joined', auto_now_add=True, blank=True)
    last_login = models.DateTimeField('last login', auto_now_add=True, blank=True)
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

    def get_username(self):
        return self.token

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'