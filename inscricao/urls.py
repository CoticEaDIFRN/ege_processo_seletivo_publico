from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin

from inscricao import views
from inscricao.services import CandidatoService

router = DefaultRouter()
router.register('candidato', CandidatoService)

app_name = 'ege_inscricao'
urlpatterns = [
    path('', views.nova_inscricao, name='nova_inscricao'),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
