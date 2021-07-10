from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from core import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.views import index, indexForNews

schema_view = get_schema_view(
    openapi.Info(
        title="Яндекс Геймификация API",
        default_version='v1',
        description="Описание моделей и запросов к БД",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', index, name='index'),
    path('news/', index, name='index'),
    path('drivers/', index, name='index'),
    path('profile/', index, name='index'),
    path('profile/order-car/', index, name='index'),
    path('prices/', index, name='index'),
    path('news/<int:id>', indexForNews, name='index'),
    path('auth/sign-in/', index, name='index'),
    path('auth/sign-up/', index, name='index'),
    path('auth/forgot-password/', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
