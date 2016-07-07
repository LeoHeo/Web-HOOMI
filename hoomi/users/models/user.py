from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from jobs.models import Job


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = self.model(
                email=self.normalize_email(email),
                **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(
            email=self.normalize_email(email),
            **kwargs
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)


class User(AbstractBaseUser, PermissionsMixin):
    job = models.ForeignKey(
        Job,
        default=2,
    )
    name = models.CharField(
            max_length=60,
    )
    email = models.EmailField(
            unique=True,
    )
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email