from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, AuthViewSet, UserViewSet, DriverViewSet, OperatorViewSet

router = DefaultRouter()

router.register(r'news', NewsViewSet, basename='news')
router.register(r'drivers', DriverViewSet, basename='drivers')
router.register(r'operators', OperatorViewSet, basename='operators')
router.register(r'users', UserViewSet, basename='users')
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path("", include(router.urls)),
]

# for url in router.urls:
#     print(url, '\n')

# urlpatterns += router.urls
