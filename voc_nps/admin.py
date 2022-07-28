from django.contrib import admin
from .models import voc_nps,Rating,Scale,Rating_Report, Account
# Register your models here.
admin.site.register(Account)
admin.site.register(voc_nps)
admin.site.register(Rating)
admin.site.register(Scale)
admin.site.register(Rating_Report)