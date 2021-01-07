from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import News, PriceList, Discount, CarType, Car, User, Driver, Operator, Order, DriverRaiting, DriverRaitingComment
import datetime
from django.urls import reverse
from django.utils.html import escape, mark_safe
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status',
                    'created_at', 'published_at')
    actions = ["make_news_published"]
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


class PriceListAdmin(admin.ModelAdmin):
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


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'discountAmount', 'promoCode')
    search_fields = ('startTown', 'endTown')
    fieldsets = ((None, {
        'fields': (
            'discountAmount',
            'promoCode',
        )
    }),)
    filter_horizontal = ()


class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'typeName', 'typeDescription')
    search_fields = ('typeName', 'typeDescription')
    fieldsets = ((None, {
        'fields': (
            'typeName',
            'typeDescription',
        )
    }),)
    filter_horizontal = ()


class CarAdmin(admin.ModelAdmin):

    def carType_link(self, obj: Car):
        link = reverse("admin:api_cartype_change", args=[obj.carType.id])
        return mark_safe(f'<a href="{link}">{escape(obj.carType.__str__())}</a>')

    carType_link.short_description = 'Тип авто'
    carType_link.admin_order_field = 'тип авто'

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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(userType__in=['admin', 'user'],)

    ordering = ('email',)
    list_filter = ()
    list_display = ('email', 'name', 'surname',
                    'date_joined', 'last_login')
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


class DriverAdmin(admin.ModelAdmin):

    def car_link(self, obj: Driver):
        link = reverse("admin:api_cartype_change", args=[obj.car.id])
        return mark_safe(f'<a href="{link}">{escape(obj.car.__str__())}</a>')

    car_link.short_description = 'Авто'
    car_link.admin_order_field = 'авто'

    list_display = ('user', 'car_link', 'phone',
                    'driverLicense', 'driverStatus')

    search_fields = ('licensePlate',)
    fieldsets = ((None, {
        'fields': (
            'car', 'phone',
            'workExperience',
            'driverLicense', 'licenseDate',
            'driverStatus'
        )
    }),)
    filter_horizontal = ()


admin.site.register(News, NewsAdmin)
admin.site.register(PriceList, PriceListAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(CarType, CarTypeAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(User, UserProfileAdmin)
admin.site.register(Driver, DriverAdmin)
