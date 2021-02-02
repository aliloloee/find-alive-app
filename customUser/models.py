from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, last_name, city, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not user_name:
            raise ValueError('Users must have an user name')
        if not first_name:
            raise ValueError('Users must have an first name')
        if not last_name:
            raise ValueError('Users must have an last name')
        if not city:
            raise ValueError('Users must have an city')

        user = self.model(
            email = self.normalize_email(email),
            user_name = user_name,
            first_name = first_name,
            last_name = last_name,
            city = city
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_name, first_name, last_name, city, password):
        user = self.create_user(
                        self.normalize_email(email),
                        user_name,
                        first_name,
                        last_name,
                        city,
                        password
                    )

        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    ## 5 necessery iputs of this custom user
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    user_name = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    ###########################

    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'city']

    def get_fullName(self) :
        return f'{self.first_name} {self.last_name}'

    def __str__(self) :
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

