from django.contrib.auth import get_user_model, password_validation
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import BaseUserManager
from rest_framework import serializers
from .models import News, PriceList, Discount, CarType, Car, User, Driver, Operator, Order, DriverRaiting, DriverRaitingComment


User = get_user_model()


class EmptySerializer(serializers.Serializer):
    pass

# ============================================
# ПОЛЬЗОВАТЕЛИ
# ============================================


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "surname",
                  "date_joined", "email", "userType"]


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "surname"]


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'surname', 'password', 'userType')

# ============================================
# НОВОСТИ
# ============================================


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "image", "description", "created_at"]


class NewsShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "created_at"]

# ============================================
# СПИСОК ЦЕН
# ============================================


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ["id", "price", "startTown", "endTown"]


# ============================================
# СКИДКИ
# ============================================
class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["id", "discountAmount", "promoCode"]


# ============================================
# ТИПЫ МАШИН
# ============================================
class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ["id", "typeName", "typeDescription"]


# ============================================
# МАШИНЫ
# ============================================
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "carType", "licensePlate",
                  "color", "brand", "releaseYear", "isPersonal"]


class CarShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "color", "brand", "licensePlate"]


# ============================================
# ВОДИТЕЛИ
# ============================================
class DriverSerializer(serializers.ModelSerializer):

    user_details = UserShortSerializer(source="user")
    car_details = CarShortSerializer(source="car")

    class Meta:
        model = Driver
        fields = ["id", "user_details", "car_details", "photo",
                  "phone", "workExperience", "driverStatus"]


class DriverShortSerializer(serializers.ModelSerializer):

    user_details = UserShortSerializer(source="user")
    car_details = CarShortSerializer(source="car")

    class Meta:
        model = Driver
        fields = ["id", "user_details", "car_details", "driverStatus"]


class DriverChangeStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ["driverStatus", ]


# ============================================
# ОПЕРАТОРЫ
# ============================================
class OperatorSerializer(serializers.ModelSerializer):

    user_details = UserShortSerializer(source="user")

    class Meta:
        model = Operator
        fields = ["id", "user_details", "photo",
                  "phone", "operatorStatus"]


class OperatorShortSerializer(serializers.ModelSerializer):

    user_details = UserShortSerializer(source="user")

    class Meta:
        model = Operator
        fields = ["id", "user_details", "operatorStatus"]


class OperatorChangeStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operator
        fields = ["operatorStatus", ]


# ============================================
# ЗАКАЗЫ
# ============================================
class OrderSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ["id", "user", "discount", "town", "street", "house", "entrance",
                  "destinationTown", "destinationStreet", "destinationHouse", "created_at", "scheduledTime"]


class OrderChangeStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ["orderStatus", ]


class OrderListSerializer(serializers.ModelSerializer):

    full_client_address = serializers.CharField(read_only=True)
    full_destination_address = serializers.CharField(read_only=True)

    user_details = UserShortSerializer(source="user", read_only=True)
    driver_details = DriverShortSerializer(source="driver", read_only=True)
    discount_details = DiscountSerializer(source="discount", read_only=True)

    class Meta:
        model = Order
        fields = ["id", "user_details", "driver_details", "discount_details", "full_client_address", "full_destination_address",
                  "price", "unauthorizedUser", "orderStatus", "created_at", "scheduledTime"]


# ============================================
# КОММЕНТАРИИ К ВОДИТЕЛЯМ
# ============================================
class DriverRaitingCommentSerializer(serializers.ModelSerializer):

    user_details = UserShortSerializer(source="user", read_only=True)
    driver_details = DriverShortSerializer(source="driver", read_only=True)

    class Meta:
        model = DriverRaitingComment
        fields = ["id", "user_details", "driver_details", "text", "created_at"]


class DriverRaitingCommentCreateSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = DriverRaitingComment
        fields = ["user", "driver", "text", ]


# ============================================
# ОЦЕНКИ ВОДИТЕЛЕЙ
# ============================================


class DriverRaitingSerializer(serializers.ModelSerializer):

    user_details = UserShortSerializer(source="user", read_only=True)
    driver_details = DriverShortSerializer(source="driver", read_only=True)

    class Meta:
        model = DriverRaiting
        fields = ["id", "user_details",
                  "driver_details", "raiting", "created_at"]


class DriverRaitingCreateSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = DriverRaiting
        fields = ["user", "driver", "raiting", ]
