
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin

from inscricao.views import RegistrarInscricaoView
from inscricao.services import CandidatoService

router = DefaultRouter()
router.register('candidato', CandidatoService)

urlpatterns = [
    path('inscricao/', RegistrarInscricaoView.as_view(), name='registrar_inscricao'),
    path('listar', RegistrarInscricaoView.lista_inscricoes, name='listar'),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    #path('candidatos/',views.authenticate_credentials),
]