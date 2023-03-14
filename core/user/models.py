import uuid
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from core.abstract.models import AbstractManager, AbstractModel


class UserManager(BaseUserManager, AbstractManager):

    def create_user(self, username, email, password=None, **kwargs):
        """Создать и вернуть `User` с email-ом, телефонным номером, логином и паролем."""
        if username is None:
            raise TypeError("У пользователя должен быть логин.")
        if email is None:
            raise TypeError("У пользователя должен быть адрес электронной почты.")
        if password is None:
            raise TypeError("Введите пароль.")

        user = self.model(
            username=username, email=self.normalize_email(email), **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **kwargs):
        """
        Создает и возвращает юзера с правами суперпользователя.
        """
        if password is None:
            raise TypeError("Введите пароль.")
        if email is None:
            raise TypeError("Введите адрес электронной почты, суперпользователя.")
        if username is None:
            raise TypeError("Введите логин, суперпользователя.")

        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)
    posts_liked = models.ManyToManyField("core_post.Post", related_name="liked_by")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def like(self, post):
        """Like `post` if it hasn't been done yet"""
        return self.posts_liked.add(post)

    def remove_like(self, post):
        """Remove a like from a `post`"""
        return self.posts_liked.remove(post)

    def has_liked(self, post):
        """Return True if the user has liked a `post`; else False"""
        return self.posts_liked.filter(pk=post.pk).exists()
