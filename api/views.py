from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, password_validation, logout, authenticate
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from .utils import get_and_authenticate_user, create_user_account
from .serializers import NewsSerializer, UserSerializer, DriverSerializer, OperatorSerializer, \
    OrderSerializer, DriverRaitingCommentSerializer, DriverRaitingSerializer, \
    DriverRaitingCreateSerializer, DriverRaitingCommentCreateSerializer, OrderListSerializer, \
    EmptySerializer, DriverShortSerializer, DriverChangeStatusSerializer, OperatorChangeStatusSerializer, \
    OperatorShortSerializer, OrderChangeStatusSerializer, PriceListSerializer, NewsShortSerializer, \
    RegistrationSerializer, LoginSerializer, CreateOrderSerializer, CurrentOrderSerializer

from .models import News, Driver, Operator, Order, \
    DriverRaitingComment, DriverRaiting, PriceList

User = get_user_model()


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        created_user = serializer.save()
        tokens = get_tokens_for_user(created_user)
        return Response({'user': serializer.data, 'tokens': tokens}, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        tokens = get_tokens_for_user(User.objects.get(email=user["email"]))
        serializer2 = UserSerializer(User.objects.get(email=user["email"]))
        return Response({'user': serializer2.data, 'tokens': tokens}, status=status.HTTP_200_OK)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserSerializer
        else:
            return EmptySerializer

    def partial_update(self, request, *args, **kwargs):
        user_object = self.get_object()
        data = request.data

        user_object.name = data.get('name', user_object.name)
        user_object.surname = data.get('surname', user_object.surname)
        user_object.phone = data.get('phone', user_object.phone)

        user_object.save()
        serializer = UserSerializer(user_object)
        return Response(serializer.data)

    def create(self, request, pk=None):
        content = {
            'NotAllowed': 'Создание водителя доступно только в админ панели'}
        return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        content = {
            'NotAllowed': 'Удаление водителя доступно только в админ панели'}
        return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)


# ============================================
# НОВОСТИ
# ============================================

class LastNewsAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        news = News.objects.filter(status__in=['published', ], ).latest("id")
        serializer = NewsShortSerializer(news, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().filter(status__in=['published', ], )

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return NewsShortSerializer
        elif self.action == 'retrieve':
            return NewsSerializer
        else:
            return EmptySerializer

    def create(self, request, pk=None):
        content = {
            'NotAllowed': 'Создание новости доступно только в админ панели'}
        return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        content = {
            'NotAllowed': 'Удаление новости доступно только в админ панели'}
        return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        content = {
            'NotAllowed': 'Изменение новости доступно только в админ панели'}
        return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)


# ============================================
# ВОДИТЕЛИ
# ============================================


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all().filter(driverStatus__in=['waiting_order', 'on_order'])

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return DriverShortSerializer
        elif self.action == 'retrieve':
            return DriverSerializer
        elif self.action == 'update':
            return DriverChangeStatusSerializer
        else:
            return EmptySerializer

    def create(self, request, pk=None):
        content = {
            'NotAllowed': 'Создание водителя доступно только в админ панели'}
        return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        content = {
            'NotAllowed': 'Удаление водителя доступно только в админ панели'}
        return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)


# ============================================
# ОПЕРАТОРЫ
# ============================================

class OperatorViewSet(viewsets.ModelViewSet):
    queryset = Operator.objects.all()

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return OperatorShortSerializer
        elif self.action == 'retrieve':
            return OperatorSerializer
        elif self.action == 'update':
            return OperatorChangeStatusSerializer
        else:
            return EmptySerializer

    def create(self, request, pk=None):
        content = {
            'NotAllowed': 'Создание оператора доступно только в админ панели'}
        return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        content = {
            'NotAllowed': 'Удаление оператора доступно только в админ панели'}
        return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)


# ============================================
# ЗАКАЗЫ
# ============================================

class getCurrentOrderAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        order = Order.objects.filter(user=request.user.id).filter(orderStatus__in=['client_waiting', 'in_progress', 'driver_waiting',], ).first()
        serializer = CurrentOrderSerializer(order, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class closeCurrentOrderAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        id = request.data.get('id', None)
        order = Order.objects.get(id=id)
        order.orderStatus = 'client_canceled'
        order.save()
        return Response( status=status.HTTP_200_OK)


class CreateOrderAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateOrderSerializer

    def post(self, request):
        order = request.data.get('order', {})
        serializer = self.serializer_class(data=order)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return OrderListSerializer
        elif self.action == 'update':
            return OrderChangeStatusSerializer
        else:
            return OrderSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def destroy(self, request, pk=None):
        content = {
            'NotAllowed': 'Удаление заказа доступно только в админ панели'}
        return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)


# ============================================
# КОММЕНТАРИИ К ВОДИТЕЛЯМ
# ============================================

class CommentViewSet(viewsets.ModelViewSet):
    queryset = DriverRaitingComment.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return DriverRaitingCommentCreateSerializer
        else:
            return DriverRaitingCommentSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


# ============================================
# ОЦЕНКИ ВОДИТЕЛЯМ
# ============================================

class RaitingViewSet(viewsets.ModelViewSet):
    queryset = DriverRaiting.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return DriverRaitingCreateSerializer
        else:
            return DriverRaitingSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


# ============================================
# СПИСОК ЦЕН
# ============================================

class PriceListViewSet(viewsets.ModelViewSet):
    queryset = PriceList.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PriceListSerializer
        else:
            return EmptySerializer

    def create(self, request, pk=None):
        content = {
            'NotAllowed': 'Создание цены маршрута доступно только в админ панели'}
        return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        content = {
            'NotAllowed': 'Удаление цены доступно только в админ панели'}
        return Response(content, status.HTTP_405_METHOD_NOT_ALLOWED)


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        try:
            token = RefreshToken(request.data["refresh_token"])
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
