from django.contrib import admin
from .models import EnterSenti

#Register your models here.

class EnterSentiAdmin(admin.ModelAdmin):
    class Meta :
        model=EnterSenti

admin.site.register(EnterSenti,EnterSentiAdmin)
