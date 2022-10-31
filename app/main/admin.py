from django.contrib import admin
from .models import News, User

# add model to admin panel
admin.site.register(News)
admin.site.register(User)