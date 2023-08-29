
from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):

    list_display = ['first_name', 'last_name',
                    'password',  'date_sign_in']
    list_filter = ['date_sign_in']
    search_fields = ['first_name', 'last_name',
                     'password', 'date_sign_in']


admin.site.register(Account, AccountAdmin)
