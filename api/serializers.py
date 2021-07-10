from django.contrib.auth import get_user_model, password_validation, authenticate
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import BaseUserManager
from rest_framework import serializers
from .models import News, PriceList, Discount, CarType, Car, User, Driver, Operator, Order, DriverRaiting, \
    DriverRaitingComment

User = get_user_model()


class EmptySerializer(serializers.Serializer):
    pass


# ============================================
# ПОЛЬЗОВАТЕЛИ
# ============================================

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'name', 'surname', 'password', 'phone', 'userType']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'surname', 'password', 'phone', 'userType']

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        # return user
        return {
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'surname': user.surname,
            'phone': user.phone,
            'userType': user.userType
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'surname', "phone", 'userType')


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "surname"]


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'surname', 'password', "phone", 'userType')


# ============================================
# НОВОСТИ
# ============================================


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "image", "content", "type", "published_at"]


class NewsShortSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = News
        fields = ["id", "title", "image", "description", "type", "published_at"]


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
        fields = ["id", "color", "brand"]


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
class CreateOrderSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    discount = serializers.CharField(allow_blank=True)
    town = serializers.CharField()
    street = serializers.CharField()
    house = serializers.IntegerField()
    entrance = serializers.IntegerField()
    destinationTown = serializers.CharField()
    destinationStreet = serializers.CharField()
    destinationHouse = serializers.CharField()
    scheduledTime = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = ["id", "user", "discount", "town", "street", "house", "entrance", "price",
                  "destinationTown", "destinationStreet", "destinationHouse", "scheduledTime"]

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def validate(self, data):
        user_id = data.get('user_id', None)
        discount = data.get('discount', None)
        town = data.get('town', None)
        entrance = data.get('entrance', None)
        street = data.get('street', None)
        house = data.get('house', None)
        destinationTown = data.get('destinationTown', None)
        destinationStreet = data.get('destinationStreet', None)
        destinationHouse = data.get('destinationHouse', None)
        scheduledTime = data.get('scheduledTime', None)
        discount_candidate = Discount.objects.filter(promoCode=discount).first()
        driver_candidate = Driver.objects.filter(driverStatus='waiting_order').first()
        if discount != '':
            if discount_candidate is None:
                raise serializers.ValidationError(
                    'Не верный промокод.'
                )
        user_candidate = User.objects.filter(id=user_id).first()
        if user_candidate is None or not user_candidate.is_active:
            raise serializers.ValidationError(
                'Не валидный пользователь.'
            )
        if town is None or street is None or house is None:
            raise serializers.ValidationError(
                'Не валидный ваш адрес.'
            )
        if destinationTown is None or destinationStreet is None or destinationHouse is None:
            raise serializers.ValidationError(
                'Не валидный адрес доставки'
            )
        if scheduledTime is None:
            raise serializers.ValidationError(
                'Не указано время'
            )

        return {
            'user': user_candidate,
            'driver': driver_candidate,
            'discount': discount_candidate,
            'price': 200,
            'unauthorizedUser': None,
            'town': town,
            'street': street,
            'house': house,
            'entrance': entrance,
            'destinationTown': destinationTown,
            'destinationStreet': destinationStreet,
            'destinationHouse': destinationHouse,
            'orderStatus': 'client_waiting',
            'scheduledTime': scheduledTime
        }


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

class CurrentOrderSerializer(serializers.ModelSerializer):
    full_client_address = serializers.CharField(read_only=True)
    full_destination_address = serializers.CharField(read_only=True)

    driver_details = DriverShortSerializer(source="driver", read_only=True)
    discount_details = DiscountSerializer(source="discount", read_only=True)

    class Meta:
        model = Order
        fields = ["id", "driver_details", "discount_details", "full_client_address",
                  "full_destination_address",
                  "price", "orderStatus", "created_at", "scheduledTime"]

class OrderListSerializer(serializers.ModelSerializer):
    full_client_address = serializers.CharField(read_only=True)
    full_destination_address = serializers.CharField(read_only=True)

    user_details = UserShortSerializer(source="user", read_only=True)
    driver_details = DriverShortSerializer(source="driver", read_only=True)
    discount_details = DiscountSerializer(source="discount", read_only=True)

    class Meta:
        model = Order
        fields = ["id", "user_details", "driver_details", "discount_details", "full_client_address",
                  "full_destination_address",
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
