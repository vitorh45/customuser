#coding: utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from forms import UsuarioCreationForm, UsuarioChangeForm
from models import Usuario

class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    #aqui no fieldsets em Personal Info precisa adicionar os campos 
    #adicionados no models
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email',
                                        'photo', 'cpf', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    class Media:
        js = (
            '/static/site/js/jquery-1.10.2.js',
            '/static/site/js/jquery.masked-input-plugin.js',
            '/static/site/js/main.js',
        )
    
admin.site.register(Usuario, UsuarioAdmin)
