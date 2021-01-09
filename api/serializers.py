from django.contrib.auth import get_user_model, password_validation
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import BaseUserManager
from rest_framework import serializers
from .models import News, PriceList, Discount, CarType, Car, User, Driver, Operator, Order, DriverRaiting, DriverRaitingComment


User = get_user_model()


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["id", "title", "image", "description", "created_at"]


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ["id", "price", "startTown", "endTown"]


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["id", "discountAmount", "promoCode"]


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = ["id", "typeName", "typeDescription"]


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "carType", "licensePlate",
                  "color", "brand", "releaseYear", "isPersonal"]


class CarShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "licensePlate"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "surname",
                  "date_joined", "email", "userType"]


# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ["name", "surname", "email", "password"]


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'name', 'surname')

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'surname',
                  'userType', 'auth_token')
        read_only_fields = ('id', 'is_active', 'is_staff')

    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError(
                'Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value


class EmptySerializer(serializers.Serializer):
    pass


class DriverSerializer(serializers.ModelSerializer):

    user_details = UserSerializer(source="user")
    car_details = CarShortSerializer(source="car")

    class Meta:
        model = Driver
        fields = ["id", "user_details", "car_details", "photo", "birthdate",
                  "phone", "workExperience", "driverLicense", "licenseDate", "driverStatus"]


class OperatorSerializer(serializers.ModelSerializer):

    user_details = UserSerializer(source="user")

    class Meta:
        model = Operator
        fields = ["id", "user_details", "photo", "birthdate",
                  "phone", "workExperience", "operatorStatus"]


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "surname"]


class DriverShortSerializer(serializers.ModelSerializer):

    user_details = UserShortSerializer(source="user")
    car_details = CarShortSerializer(source="car")

    class Meta:
        model = Driver
        fields = ["id", "user_details", "car_details"]


class OperatorShortSerializer(serializers.ModelSerializer):

    user_details = UserShortSerializer(source="user")

    class Meta:
        model = Operator
        fields = ["id", "user_details"]


class OrderSerializer(serializers.ModelSerializer):

    full_client_address = serializers.CharField(read_only=True)
    full_destination_address = serializers.CharField(read_only=True)

    user_details = UserShortSerializer(source="user", read_only=True)
    driver_details = DriverShortSerializer(source="driver", read_only=True)
    discount_details = DiscountSerializer(source="discount", read_only=True)

    class Meta:
        model = Order
        fields = ["id", "user_details", "driver_details", "discount_details", "full_client_address", "full_destination_address",
                  "price", "unauthorizedUser", "town", "street", "house", "entrance",
                  "destinationTown", "destinationStreet", "destinationHouse", "orderStatus", "created_at", "scheduledTime"]


class DriverRaitingCommentSerializer(serializers.ModelSerializer):

    user_details = UserShortSerializer(source="user", read_only=True)
    driver_details = DriverShortSerializer(source="driver", read_only=True)

    class Meta:
        model = DriverRaitingComment
        fields = ["id", "user_details", "driver_details", "text", "created_at"]


class DriverRaitingSerializer(serializers.ModelSerializer):

    user_details = UserShortSerializer(source="user", read_only=True)
    driver_details = DriverShortSerializer(source="driver", read_only=True)

    class Meta:
        model = DriverRaiting
        fields = ["id", "user_details",
                  "driver_details", "raiting", "created_at"]
