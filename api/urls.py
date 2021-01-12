from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, DriverViewSet, \
    OperatorViewSet, OrderViewSet, CommentViewSet, RaitingViewSet, \
    PriceListViewSet

router = DefaultRouter()

router.register(r'news', NewsViewSet, basename='news')
router.register(r'drivers', DriverViewSet, basename='drivers')
router.register(r'operators', OperatorViewSet, basename='operators')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'drivers-raiting', RaitingViewSet, basename='drivers-raiting')
router.register(r'drivers-comments', CommentViewSet,
                basename='drivers-comments')
router.register(r'price-list', PriceListViewSet, basename='price-list')

urlpatterns = [
    path("", include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path("rest-auth/", include('rest_framework.urls')),
]
