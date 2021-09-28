"""django_fr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from fr import views
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

login = views.LoginView.as_view({'get':'get'}, )

router = routers.DefaultRouter()
router.register(r'opros', views.OprosViewList,'opros')
router.register(r'vopros', views.VoprosViewList, 'vopros')
router.register(r'otvet', views.OtvetViewList, 'otvet')
router.register(r'useropros', views.OprosViewReadOnly, 'useropros')
router.register(r'uservopros', views.VoprosViewReadOnly, 'uservopros')
router.register('userotvets', views.SetOtvet, 'userotvets')
router.register('login', views.LoginView, 'login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('doc-api/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='doc-api'),
    path('openapi', get_schema_view(
        title="Тестовое задание",
        description="Описание API",
        version="1.0.0"
    ), name='openapi-schema'),
]

print(f' router.urls = {router.urls}')