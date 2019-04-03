from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.contrib.auth import views as auth_views

from cadastro.views import RegistrarCadastroView, Logar
# from inscricao.services import CandidatoService

# router = DefaultRouter()
# router.register('candidato', CandidatoService)


urlpatterns = [
    path('registrar/', RegistrarCadastroView.as_view(), name="registrar"),
    # path('api/v1/', include(router.urls)),
    #path('admin/', admin.site.urls),
    path('index/', RegistrarCadastroView.index, name="index"),
    path('listar/', RegistrarCadastroView.lista_cadastros, name="listar"),
    path('entrar/', Logar.as_view(), name="login")

]
