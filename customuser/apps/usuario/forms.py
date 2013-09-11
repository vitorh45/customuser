#coding: utf-8 
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from models import Usuario


class UsuarioCreationForm(UserCreationForm):

    class Meta:
        model = Usuario
        
class UsuarioChangeForm(UserChangeForm):
    
    class Meta:
        model = Usuario    
