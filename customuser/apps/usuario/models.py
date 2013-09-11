#coding: utf-8 
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    #aqui adiciona os campos adicionais
    photo = models.ImageField('Foto', upload_to='usuario', null=True, blank=True)
    cpf = models.CharField('CPF', null=True, blank=True, max_length=11)
    rg = models.CharField('RG', null=True, blank=True, max_length=10)
    
    class Meta:
        abstract = False
        verbose_name = u'Usuário'
        verbose_name_plural = u'Usuários'

