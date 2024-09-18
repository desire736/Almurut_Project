from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractUser):

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        unique=True,
        db_index=True
    )

    avatar = models.ImageField(upload_to='avatars/')
    birthdate = models.DateField(null=True)

    phone_number = models.CharField(
            max_length=22,
            null=True,
            blank=True
        )

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        unique_together = ('first_name', 'last_name',)


class ProductUserRating:
    pass
