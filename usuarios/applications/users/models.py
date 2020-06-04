from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    
    # Opciones de los atributos:
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    # Atributos:
    username = models.CharField(max_length=10, unique=True)
    
    email = models.EmailField()

    nombres = models.CharField(max_length=30)

    apellidos = models.CharField(max_length=30)

    genero = models.CharField(max_length=1, choices=GENEROS, blank=True)

    USERNAME_FIELD = 'username'

    class Meta:
    
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    def get_short_name(self):
        return self.username


    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos

