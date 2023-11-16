from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email_adress',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)

    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_admin(self):
        return self.admin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email adress')
        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_staffuser(self,email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self.db)
        return user

    def create_superuser(self,email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self.db)
        return user
