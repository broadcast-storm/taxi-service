from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class News(models.Model):
    title = models.CharField(
        max_length=200, verbose_name="Название новости", unique=True)
    description = models.TextField(
        verbose_name="Описание новости")
    image = models.ImageField(verbose_name="Картинка новости")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"

    def __str__(self):
        return self.title


class PriceList(models.Model):
    price = models.IntegerField(default=0, verbose_name="Цена")
    startTown = models.CharField(
        max_length=200, verbose_name="Начальный насел. пункт", unique=True)
    endTown = models.CharField(
        max_length=200, verbose_name="Конечный насел. пункт", unique=True)

    class Meta:
        verbose_name = "цена"
        verbose_name_plural = "цены"

    def __str__(self):
        return self.startTown + " - " + self.endTown


class Discount(models.Model):
    discountAmount = models.IntegerField(default=0, verbose_name="Скидка в %")
    promoCode = models.CharField(
        max_length=200, verbose_name="Промокод", unique=True)

    class Meta:
        verbose_name = "скидка"
        verbose_name_plural = "скидки"

    def __str__(self):
        return self.promoCode


class CarType(models.Model):
    typeName = models.CharField(
        max_length=120, verbose_name="Тип машины", unique=True)
    typeDescription = models.TextField(
        verbose_name="Описание типа")

    class Meta:
        verbose_name = "тип машины"
        verbose_name_plural = "типы машин"

    def __str__(self):
        return self.typeName


class Car(models.Model):
    YELLOW = 'yellow'
    GREEN = 'green'
    RED = 'red'
    BLACK = 'black'
    WHITE = 'white'
    BLUE = 'blue'
    COLOR_CHOICES = (
        (YELLOW, 'жёлтый'),
        (GREEN, 'зелёный'),
        (RED, 'красный'),
        (BLACK, 'черный'),
        (WHITE, 'белый'),
        (BLUE, 'синий'),
    )

    BMW = 'BMW'
    LADA = 'LADA'
    CHEVROLET = 'CHEVROLET'
    HYUNDAI = 'HYUNDAI'
    MERSEDES = 'MERSEDES'
    PEUGEOT = 'PEUGEOT'
    BRAND_CHOICES = (
        (BMW, 'BMW'),
        (LADA, 'Lada'),
        (CHEVROLET, 'Chevrolet'),
        (HYUNDAI, 'Hyundai'),
        (MERSEDES, 'Mersedes'),
        (PEUGEOT, 'Peugeot'),
    )

    carType = models.ForeignKey(
        CarType, on_delete=models.CASCADE, verbose_name="Тип авто", )

    licensePlate = models.CharField(
        max_length=120, verbose_name="Номер авто", unique=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default=WHITE,
                             verbose_name="Цвет авто", )
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES, default=LADA,
                             verbose_name="Бренд", )
    releaseYear = models.DateTimeField(verbose_name="Год выпуска")
    isPersonal = models.BooleanField(default=False, verbose_name="Личное авто")

    class Meta:
        verbose_name = "машина"
        verbose_name_plural = "машины"

    def __str__(self):
        return self.licensePlate


class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, surname, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have an name')
        if not surname:
            raise ValueError('Users must have an surname')

        user = self.model(
            email=self.normalize_email(email),
            surname=surname,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, surname, password=None):

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            surname=surname,
            name=name,
        )
        user.is_admin = True
        user.userType = 'admin'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    ADMIN = 'admin'
    USER = 'user'
    DRIVER = 'driver'
    OPERATOR = 'operator'
    USER_TYPE_CHOICES = (
        (ADMIN, 'Администратор'),
        (USER, 'Пользователь'),
        (DRIVER, 'Водитель'),
        (OPERATOR, 'Оператор'),
    )

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name="Зарегистрировался")
    last_login = models.DateTimeField(auto_now=True, verbose_name="Был в сети")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    objects = UserProfileManager()

    userType = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=USER,
                                verbose_name="Тип пользователя")

    name = models.CharField(max_length=100, blank=True, verbose_name="Имя")
    surname = models.CharField(
        max_length=100, blank=True, verbose_name="Фамилия")
    birthDate = models.DateField(
        blank=True, null=True, verbose_name="Дата рождения")

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.name + ' ' + self.surname

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Driver(models.Model):
    photo = models.ImageField(verbose_name="Фото водителя")

    class Meta:
        verbose_name = "тип машины"
        verbose_name_plural = "типы машин"

    # def __str__(self):
    #     return self.id
