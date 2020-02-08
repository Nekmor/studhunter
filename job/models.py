from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, last_name, middle_name, phone_number, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            last_name=last_name,
            middle_name=middle_name,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, last_name, middle_name, phone_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            last_name=last_name,
            middle_name=middle_name,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='Электронная почта', max_length=60, unique=True)
    username = models.CharField(verbose_name='Имя пользователя', max_length=30, unique=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30)
    middle_name = models.CharField(verbose_name='Отчество', max_length=30)
    phone_number = models.CharField(verbose_name='Телефонный номер', max_length=12)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name', 'middle_name', 'phone_number']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Job(models.Model):
    title = models.CharField(verbose_name='Название работы', max_length=64, db_index=True)
    num = models.IntegerField(verbose_name='Количество людей')
    find = models.IntegerField(verbose_name='Найдено людей')
    salary = models.IntegerField(verbose_name='Бюджет')
    body = models.CharField(verbose_name='Описание работы', max_length=64)
    date_end = models.DateTimeField(verbose_name='Когда нужно сделать')
    user = models.ForeignKey(Account, verbose_name='Пользователь', on_delete=models.CASCADE)