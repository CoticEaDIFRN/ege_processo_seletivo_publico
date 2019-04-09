from django.db import models
from django.db.models import Model, ForeignKey, OneToOneField, CASCADE
from django.db.models import CharField, BooleanField, URLField, PositiveIntegerField, DateTimeField, DateField, DecimalField, FloatField, EmailField
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Usuario(AbstractBaseUser, PermissionsMixin):
    cpf = CharField('CPF', max_length=150, primary_key=True)
    nome = models.TextField('Nome', max_length=150)
    email = models.EmailField(_('email address'))
    senha = models.CharField(max_length=50)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    REQUIRED_FIELDS = ['nome', 'email']
    USERNAME_FIELD = 'cpf'

    def __str__(self):
        return " %s - %s " % (self.cpf, self.nome)



#.setpassword()
