"""Booker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
#-------------------------------------------------
from rest_framework import routers #REST
from Confronto.api.viewsets import ConfrontoViewSet
from Historico.api.viewsets import HistoricoViewSet
from Cenografo.viewsets.viewsets import CenografoViewSet
from Cientista.api.viewsets import CientistaViewSet
from Cientista.api.views.views import CientistaView
from MaosPossiveis.viewsets.viewsets import MaosPossiveisViewSet
#-----------------------------


router = routers.DefaultRouter()
router.register(r'confronto',ConfrontoViewSet, base_name='Confronto')
router.register(r'historico',HistoricoViewSet, base_name='historico')
router.register(r'cenografo',CenografoViewSet, base_name='cenografo')
router.register(r'cientista',CientistaViewSet, base_name='cientista')
router.register(r'maos_possiveis',MaosPossiveisViewSet, base_name='maos_possiveis')


urlpatterns = [
    path('api/v1/',include(router.urls)),
    path(r'api/v1/cientista_analizar', CientistaView.as_view()),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
