from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):


    email = models.EmailField(unique=True)
    avatar = models.ImageField()
    birthdate = models.DateField()
    phone_number = models.CharField(
            max_length=22,
            null=True,
            blank=True
        )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        unique_together = ('first_name', 'last_name',)



