from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import News, PriceList, Discount, CarType, Car, User, Driver, Operator, Order, DriverRaiting, DriverRaitingComment
import datetime
from django.urls import reverse
from django.utils.html import escape, mark_safe
from django_reverse_admin import ReverseModelAdmin

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
# Register your models here.


class NewsResource(resources.ModelResource):

    class Meta:
        model = News


class NewsAdmin(ImportExportActionModelAdmin):
    resource_class = NewsResource
    list_filter = ('status',)
    list_display = ('title', 'description', 'status',
                    'created_at', 'published_at')
    actions = ImportExportActionModelAdmin.actions + ["make_news_published", ]
    search_fields = ('title', 'description')
    fieldsets = ((None, {
        'fields': (
            'title',
            'image',
            'description',
        )
    }),)
    filter_horizontal = ()

    def make_news_published(self, request, queryset):
        rows_updated = queryset.update(
            status='published', published_at=datetime.datetime.now())
        message_bit = ""
        if rows_updated == 1:
            message_bit = "1 новости"
        else:
            message_bit = "%s новостей" % rows_updated
        self.message_user(
            request, "успешная публикация %s." % message_bit)

    make_news_published.short_description = "Опубликовать выбранные новости"


class PriceListResource(resources.ModelResource):

    class Meta:
        model = PriceList


class PriceListAdmin(ImportExportActionModelAdmin):
    resource_class = PriceListResource
    list_display = ('id', 'startTown', 'endTown', 'price')
    search_fields = ('startTown', 'endTown')
    fieldsets = ((None, {
        'fields': (
            'startTown',
            'endTown',
            'price',
        )
    }),)
    filter_horizontal = ()


class DiscountResource(resources.ModelResource):

    class Meta:
        model = Discount


class DiscountAdmin(ImportExportActionModelAdmin):
    resource_class = DiscountResource
    list_display = ('id', 'discountAmount', 'promoCode')
    search_fields = ('startTown', 'endTown')
    fieldsets = ((None, {
        'fields': (
            'discountAmount',
            'promoCode',
        )
    }),)
    filter_horizontal = ()


class CarTypeResource(resources.ModelResource):

    class Meta:
        model = CarType


class CarTypeAdmin(ImportExportActionModelAdmin):
    resource_class = CarTypeResource
    list_display = ('id', 'typeName', 'typeDescription')
    search_fields = ('typeName', 'typeDescription')
    fieldsets = ((None, {
        'fields': (
            'typeName',
            'typeDescription',
        )
    }),)
    filter_horizontal = ()


class CarResource(resources.ModelResource):
    carType = fields.Field(column_name="carType", attribute="carType",
                           widget=ForeignKeyWidget(CarType, 'typeName'))

    class Meta:
        model = Car


class CarAdmin(ImportExportActionModelAdmin):
    resource_class = CarResource

    def carType_link(self, obj: Car):
        if obj.carType == None:
            return 'Не указан тип'
        link = reverse("admin:api_cartype_change", args=[obj.carType.id])
        return mark_safe(f'<a href="{link}">{escape(obj.carType.__str__())}</a>')

    carType_link.short_description = 'Тип авто'
    carType_link.admin_order_field = 'тип авто'
    list_filter = ('brand', 'carType')
    list_display = ('licensePlate', 'color', 'brand',
                    'releaseYear', 'carType_link', 'isPersonal')
    search_fields = ('licensePlate',)
    fieldsets = ((None, {
        'fields': (
            'licensePlate', 'color',
            'brand', 'releaseYear',
            'carType', 'isPersonal'
        )
    }),)
    filter_horizontal = ()


class UserProfileAdmin(UserAdmin):

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(userType__in=['admin', 'user'],)

    ordering = ('email',)
    list_filter = ('userType',)
    list_display = ('email', 'name', 'surname',
                    'date_joined', 'last_login', 'userType')
    search_fields = ('name', 'surname')
    readonly_fields = ('date_joined', 'last_login')
    fieldsets = (
        (None, {'fields': ('name', 'surname', "email",
                           "last_login", "date_joined", 'password')}),
    )
    add_fieldsets = (
        (None, {'fields': ("email", 'name', 'surname', 'password1', 'password2')}),
    )

    filter_horizontal = ()


class UserInline(admin.TabularInline):
    model = User
    fieldsets = (
        (None, {'fields': ('name', 'surname', "email", 'userType',
                           "last_login", "date_joined")}),
    )
    readonly_fields = ('date_joined', 'last_login')

    def has_delete_permission(self, request, obj=None):
        return False


class DriverAdmin(ReverseModelAdmin):

    inline_type = 'stacked'
    inline_reverse = [
        {
            'field_name': 'user',
            'admin_class': UserInline
        },

    ]

    def car_link(self, obj: Driver):
        if obj.car == None:
            return 'Без машины'
        link = reverse("admin:api_car_change", args=[obj.car.id])
        return mark_safe(f'<a href="{link}">{escape(obj.car.__str__())}</a>')

    car_link.short_description = 'Авто'
    car_link.admin_order_field = 'авто'
    list_filter = ('driverStatus',)
    list_display = ('user', 'car_link', 'phone',
                    'driverLicense', 'driverStatus')


class OperatorAdmin(ReverseModelAdmin):
    inline_type = 'stacked'
    inline_reverse = [
        {
            'field_name': 'user',
            'admin_class': UserInline
        },
    ]
    list_filter = ('operatorStatus',)
    list_display = ('user', 'phone', 'operatorStatus')


class OrderResource(resources.ModelResource):
    user = fields.Field(column_name="user", attribute="user",
                        widget=ForeignKeyWidget(User, 'surname'))
    driver = fields.Field(column_name="driver", attribute="driver",
                          widget=ForeignKeyWidget(Driver, "user"))
    discount = fields.Field(column_name="discount", attribute="discount",
                            widget=ForeignKeyWidget(Discount, 'discountAmount'))

    class Meta:
        model = Order


class OrderAdmin(ImportExportActionModelAdmin):
    resource_class = OrderResource

    def user_link(self, obj: Order):
        if obj.user == None:
            return 'Нет в приложении'
        link = reverse("admin:api_user_change", args=[obj.user.id])
        return mark_safe(f'<a href="{link}">{escape(obj.user.__str__())}</a>')

    user_link.short_description = 'Клиент'
    user_link.admin_order_field = 'клиент'

    def driver_link(self, obj: Order):
        if obj.driver == None:
            return 'Нет водителя'
        link = reverse("admin:api_driver_change", args=[obj.driver.id])
        return mark_safe(f'<a href="{link}">{escape(obj.driver.__str__())}</a>')

    driver_link.short_description = 'Водитель'
    driver_link.admin_order_field = 'водитель'

    def discount_link(self, obj: Order):
        if obj.discount == None:
            return 'Без скидки'
        link = reverse("admin:api_discount_change", args=[obj.discount.id])
        return mark_safe(f'<a href="{link}">{escape(obj.discount.__str__())}</a>')

    discount_link.short_description = 'Скидка'
    discount_link.admin_order_field = 'скидка'

    def unauthorized(self, obj: Order):
        if obj.user == None:
            return obj.unauthorizedUser
        return 'Есть в приложении'

    unauthorized.short_description = 'Неавторизованный клиент'
    unauthorized.admin_order_field = 'неавторизованный клиент'

    def client_address(self, obj: Order):
        address_line = obj.town + " ул. " + obj.street + \
            " д. " + obj.house + " под." + str(obj.entrance)
        return address_line

    client_address.short_description = 'Адрес клиента'
    client_address.admin_order_field = 'адрес клиента'

    def destination_address(self, obj: Order):
        address_line = obj.destinationTown + " ул. " + \
            obj.destinationStreet + " д. " + obj.destinationHouse
        return address_line

    destination_address.short_description = 'Конечный адрес'
    destination_address.admin_order_field = 'конечный адрес'
    list_filter = ('orderStatus',)
    list_display = ("id", 'user_link', 'unauthorized', 'driver_link', 'discount_link', 'price',
                    'client_address', 'destination_address', "orderStatus", "scheduledTime", "created_at")
    search_fields = ('town', 'destinationTown')
    # fieldsets = ((None, {
    #     'fields': (
    #         'licensePlate', 'color',
    #         'brand', 'releaseYear',
    #         'carType', 'isPersonal'
    #     )
    # }),)
    filter_horizontal = ()


class DriverRaitingCommentAdmin(admin.ModelAdmin):
    def user_link(self, obj: DriverRaitingComment):
        if obj.user == None:
            return 'Нет в приложении'
        link = reverse("admin:api_user_change", args=[obj.user.id])
        return mark_safe(f'<a href="{link}">{escape(obj.user.__str__())}</a>')

    user_link.short_description = 'Клиент'
    user_link.admin_order_field = 'клиент'

    def driver_link(self, obj: DriverRaitingComment):
        if obj.driver == None:
            return 'Нет водителя'
        link = reverse("admin:api_driver_change", args=[obj.driver.id])
        return mark_safe(f'<a href="{link}">{escape(obj.driver.__str__())}</a>')

    driver_link.short_description = 'Водитель'
    driver_link.admin_order_field = 'водитель'

    list_display = ('id', 'user_link', 'driver_link', 'text', 'created_at')
    search_fields = ('text',)
    readonly_fields = ('user', 'driver', 'text', 'created_at')
    filter_horizontal = ()


class DriverRaitingAdmin(admin.ModelAdmin):
    def user_link(self, obj: DriverRaiting):
        if obj.user == None:
            return 'Нет в приложении'
        link = reverse("admin:api_user_change", args=[obj.user.id])
        return mark_safe(f'<a href="{link}">{escape(obj.user.__str__())}</a>')

    user_link.short_description = 'Клиент'
    user_link.admin_order_field = 'клиент'

    def driver_link(self, obj: DriverRaiting):
        if obj.driver == None:
            return 'Нет водителя'
        link = reverse("admin:api_driver_change", args=[obj.driver.id])
        return mark_safe(f'<a href="{link}">{escape(obj.driver.__str__())}</a>')

    driver_link.short_description = 'Водитель'
    driver_link.admin_order_field = 'водитель'

    list_display = ('id', 'user_link', 'driver_link', 'raiting', 'created_at')

    readonly_fields = ('user', 'driver', 'raiting', 'created_at')
    filter_horizontal = ()


admin.site.register(News, NewsAdmin)
admin.site.register(PriceList, PriceListAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(CarType, CarTypeAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(User, UserProfileAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Operator, OperatorAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(DriverRaitingComment, DriverRaitingCommentAdmin)
admin.site.register(DriverRaiting, DriverRaitingAdmin)
