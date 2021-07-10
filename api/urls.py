from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, DriverViewSet, \
    OperatorViewSet, OrderViewSet, CommentViewSet, RaitingViewSet, \
    PriceListViewSet, LogoutAllView, LogoutView, RegistrationAPIView, LoginAPIView, LastNewsAPIView, CreateOrderAPIView, \
    UsersViewSet, getCurrentOrderAPIView, closeCurrentOrderAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()



router.register(r'news', NewsViewSet, basename='news')
router.register(r'users', UsersViewSet, basename='users')
router.register(r'drivers', DriverViewSet, basename='drivers')
router.register(r'operators', OperatorViewSet, basename='operators')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'drivers-raiting', RaitingViewSet, basename='drivers-raiting')
router.register(r'drivers-comments', CommentViewSet,
                basename='drivers-comments')
router.register(r'price-list', PriceListViewSet, basename='price-list')

urlpatterns = [
    path("", include(router.urls)),
    path('create-user', RegistrationAPIView.as_view(), name='create-user'),
    path('create-order', CreateOrderAPIView.as_view(), name='create-order'),
    path('current-order', getCurrentOrderAPIView.as_view(), name='current-order'),
    path('close-order', closeCurrentOrderAPIView.as_view(), name='close-order'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='auth_logout'),
    path('logout-all', LogoutAllView.as_view(), name='auth_logout_all'),
    path('refresh-token', TokenRefreshView.as_view(), name='refresh-token'),
    path('last-news', LastNewsAPIView.as_view(), name='last-news'),
]
