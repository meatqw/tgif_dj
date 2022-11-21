from django.contrib import admin
from .models import *

# add models to admin panel
admin.site.register(News, NewsAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Wallets, WalletsAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(ExchangeRates, ExchangeRatesAdmin)
admin.site.register(Tg)
admin.site.register(Status)