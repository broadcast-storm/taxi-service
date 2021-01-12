from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date

# ============================================
# НОВОСТИ
# ============================================


class News(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = (
        (DRAFT, 'Черновик'),
        (PUBLISHED, 'Опубликована'),
    )

    title = models.CharField(
        max_length=200, verbose_name="Название новости", unique=True)
    description = models.TextField(
        verbose_name="Описание новости", blank=True)
    image = models.ImageField(
        verbose_name="Картинка новости", null=True, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DRAFT,
                              verbose_name="Статус новости")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")

    published_at = models.DateTimeField(
        blank=True, null=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"

    def __str__(self):
        return self.title


# ============================================
# СПИСОК ЦЕН
# ============================================

class PriceList(models.Model):
    TOWN_CHOICES = (
        ('Ramenskoe', 'Раменское'),
        ('Kratovo', 'Кратово'),
        ('Zukovski', 'Жуковский'),
        ('Bronici', 'Бронницы'),
        ('Minino', 'Минино'),
        ('Ghel', 'Гжель'),
        ('Kosherovo', 'Кошерово'),
        ('Konyashino', 'Коняшино'),
    )
    price = models.IntegerField(default=150, validators=[MinValueValidator(
        150), MaxValueValidator(10000)],  verbose_name="Цена")
    startTown = models.CharField(
        max_length=200, verbose_name="Начальный насел. пункт", choices=TOWN_CHOICES, default='Ramenskoe')
    endTown = models.CharField(
        max_length=200, verbose_name="Конечный насел. пункт", choices=TOWN_CHOICES, default='Ramenskoe', )

    class Meta:
        verbose_name = "цена"
        verbose_name_plural = "цены"

    def __str__(self):
        return self.startTown + " - " + self.endTown


# ============================================
# СКИДКИ
# ============================================

class Discount(models.Model):
    discountAmount = models.IntegerField(default=0, validators=[MinValueValidator(
        0), MaxValueValidator(100)],  verbose_name="Скидка в %")
    promoCode = models.CharField(
        max_length=6, verbose_name="Промокод", unique=True, validators=[RegexValidator(r'^[A-Z0-9]*$', 'Можно использовать буквы A-Z и цифры 0-9')])

    class Meta:
        verbose_name = "скидка"
        verbose_name_plural = "скидки"

    def __str__(self):
        return str(self.discountAmount) + "%"


# ============================================
# ТИПЫ МАШИН
# ============================================

class CarType(models.Model):
    typeName = models.CharField(
        max_length=120, verbose_name="Тип машины", unique=True)
    typeDescription = models.TextField(
        verbose_name="Описание типа", blank=True)

    class Meta:
        verbose_name = "тип машины"
        verbose_name_plural = "типы машин"

    def __str__(self):
        return self.typeName


# ============================================
# МАШИНЫ
# ============================================

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
        CarType, on_delete=models.CASCADE, verbose_name="Тип авто")

    licensePlate = models.CharField(
        max_length=9, validators=[RegexValidator(r'^[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}\d{2,3}$', 'Пример номера: А123ВЕ456')], verbose_name="Номер авто")
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default=WHITE,
                             verbose_name="Цвет авто")
    brand = models.CharField(max_length=20, choices=BRAND_CHOICES, default=LADA,
                             verbose_name="Бренд", )
    releaseYear = models.DateField(
        verbose_name="Дата выпуска", default=date.today)
    isPersonal = models.BooleanField(default=False, verbose_name="Личное авто")

    class Meta:
        verbose_name = "машина"
        verbose_name_plural = "машины"

    def __str__(self):
        return self.licensePlate


# ============================================
# ИНДИВИДУАЛЬНАЯ МОДЕЛЬ ПОЛЬЗОВАТЕЛЯ
# ============================================
class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, surname, password=None,  **extra_fields):
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
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, surname, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('userType', 'admin')

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            surname=surname,
            name=name,
            **extra_fields
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
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
    is_admin = models.BooleanField(
        default=False, verbose_name="Может вносить изменения в данные")
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        default=False, verbose_name="Доступ в админ панель")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    objects = UserProfileManager()

    userType = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=USER,
                                verbose_name="Тип пользователя")

    name = models.CharField(max_length=100, blank=True, verbose_name="Имя")
    surname = models.CharField(
        max_length=100, blank=True, verbose_name="Фамилия")

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.name + ' ' + self.surname

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


# ============================================
# ВОДИТЕЛИ
# ============================================

class Driver(models.Model):
    ON_ORDER = 'on_order'
    WAITING_ORDER = 'waiting_order'
    ON_SICK_LEAVE = 'on_sick_leave'
    ON_VACATION = 'on_vacation'
    NONWORKING_TIME = 'nonworking_time'
    FIRED = 'fired'
    DRIVER_STATUS_CHOICES = (
        (ON_ORDER, 'Выполняет заказ'),
        (WAITING_ORDER, 'В ожидании заказа'),
        (ON_SICK_LEAVE, 'На больничном'),
        (ON_VACATION, 'В отпуске'),
        (NONWORKING_TIME, 'Нерабочее время'),
        (FIRED, 'Уволен'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        unique=True,
        verbose_name="ФИО"
    )
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, verbose_name="Машина", null=True, blank=True, )
    photo = models.ImageField(
        verbose_name="Фото водителя", blank=True, null=True)
    birthdate = models.DateField(
        verbose_name="Дата рождения",)
    phone = PhoneNumberField(
        unique=True, verbose_name="Телефон")
    workExperience = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)],  verbose_name="Опыт работы (кол-во лет)")
    driverLicense = models.CharField(
        max_length=100, verbose_name="Водительские права", validators=[RegexValidator(r'^[A-Z](?:\d[- ]*){14}$', 'Пример водительских прав: D6101-40706-60905')],  unique=True)
    licenseDate = models.DateField(
        verbose_name="Дата получения прав")
    driverStatus = models.CharField(max_length=30, choices=DRIVER_STATUS_CHOICES, default=NONWORKING_TIME,
                                    verbose_name="Статус водителя")

    class Meta:
        verbose_name = "водитель"
        verbose_name_plural = "водители"

    def __str__(self):
        return str(self.user)


# ============================================
# ОПЕРАТОРЫ
# ============================================

class Operator(models.Model):
    SERVE_CLIENT = 'serve_client'
    WAITING = 'waiting'
    ON_SICK_LEAVE = 'on_sick_leave'
    ON_VACATION = 'on_vacation'
    NONWORKING_TIME = 'nonworking_time'
    FIRED = 'fired'
    OPERATOR_STATUS_CHOICES = (
        (SERVE_CLIENT, 'Обслуживает клиента'),
        (WAITING, 'В ожидании'),
        (ON_SICK_LEAVE, 'На больничном'),
        (ON_VACATION, 'В отпуске'),
        (NONWORKING_TIME, 'Нерабочее время'),
        (FIRED, 'Уволен'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        unique=True,
        verbose_name="ФИО"
    )
    photo = models.ImageField(
        verbose_name="Фото оператора", blank=True, null=True)
    birthdate = models.DateField(
        verbose_name="Дата рождения")
    phone = PhoneNumberField(
        unique=True, verbose_name="Телефон")
    workExperience = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)],  verbose_name="Опыт работы (кол-во лет)")
    operatorStatus = models.CharField(max_length=30, choices=OPERATOR_STATUS_CHOICES, default=NONWORKING_TIME,
                                      verbose_name="Статус оператора")

    class Meta:
        verbose_name = "оператор"
        verbose_name_plural = "операторы"

    def __str__(self):
        return str(self.user)


# ============================================
# ЗАКАЗЫ
# ============================================

class Order(models.Model):
    CLIENT_WAITING = 'client_waiting'
    DRIVER_WAITING = 'driver_waiting'
    CLIENT_CANCELED = 'client_canceled'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    ORDER_STATUS_CHOICES = (
        (CLIENT_WAITING, 'клиент ждет машину'),
        (DRIVER_WAITING, 'водитель ожидает клиента'),
        (CLIENT_CANCELED, 'клиент отменил заказ'),
        (IN_PROGRESS, 'клиента отвозят'),
        (COMPLETED, 'заказ выполнен'),
    )

    TOWN_CHOICES = (
        ('Ramenskoe', 'Раменское'),
        ('Kratovo', 'Кратово'),
        ('Zukovski', 'Жуковский'),
        ('Bronici', 'Бронницы'),
        ('Minino', 'Минино'),
        ('Ghel', 'Гжель'),
        ('Kosherovo', 'Кошерово'),
        ('Konyashino', 'Коняшино'),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Клиент", null=True, blank=True, )
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE, verbose_name="Водитель", null=True, blank=True, )
    discount = models.ForeignKey(
        Discount, on_delete=models.CASCADE, verbose_name="Скидка", null=True, blank=True, )
    price = models.IntegerField(default=0, verbose_name="Цена")
    unauthorizedUser = models.CharField(
        null=True, blank=True, max_length=100, verbose_name="Неавторизованный клиент")
    town = models.CharField(
        max_length=100, verbose_name="Город", choices=TOWN_CHOICES, default='Ramenskoe')
    street = models.CharField(
        max_length=100, verbose_name="Улица")
    house = models.IntegerField(default=1, validators=[
                                MinValueValidator(1)], verbose_name="Дом")
    entrance = models.IntegerField(
        default=1, validators=[MinValueValidator(1)], verbose_name="Подъезд")
    destinationTown = models.CharField(
        max_length=100, verbose_name="Город", choices=TOWN_CHOICES, default='Ramenskoe')
    destinationStreet = models.CharField(
        max_length=100, verbose_name="Улица")
    destinationHouse = models.IntegerField(
        default=1, validators=[MinValueValidator(1)], verbose_name="Дом")
    orderStatus = models.CharField(max_length=30, choices=ORDER_STATUS_CHOICES, default=CLIENT_WAITING,
                                   verbose_name="Статус заказа")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время оформления")
    scheduledTime = models.DateTimeField(
        verbose_name="Когда забрать клиента", null=True, blank=True,)

    @property
    def full_client_address(self):
        address_line = self.town + " ул. " + self.street + \
            " д. " + self.house + " под." + str(self.entrance)
        return address_line

    @property
    def full_destination_address(self):
        address_line = self.destinationTown + " ул. " + \
            self.destinationStreet + " д. " + self.destinationHouse
        return address_line

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def __str__(self):
        return str(self.id)


# ============================================
# КОММЕНТАРИИ К ВОДИТЕЛЯМ
# ============================================

class DriverRaitingComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Клиент")
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE, verbose_name="Водитель", )
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "комментарий клиента"
        verbose_name_plural = "комментарии клиентов"

    def __str__(self):
        return str(self.id)


# ============================================
# ОЦЕНКИ ВОДИТЕЛЕЙ
# ============================================

class DriverRaiting(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Клиент",)
    driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE, verbose_name="Водитель",)
    raiting = models.IntegerField(default=5, validators=[MinValueValidator(
        0), MaxValueValidator(5)], verbose_name="Оценка клиента")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "оценка клиента"
        verbose_name_plural = "оценки клиентов"

    def __str__(self):
        return str(self.id)
