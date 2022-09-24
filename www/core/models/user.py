from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    phone = PhoneNumberField(_("Phone Number"), region="KZ", blank=True)
    password = models.CharField(_("Password"), max_length=30)
    is_staff = models.BooleanField(_("Admin"), default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELD = ["phone", "password"]

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if isinstance(self.email, str):
            if self.email:
                self.email = self.email.lower()
            else:
                self.email = None
        super().save(*args, **kwargs)
