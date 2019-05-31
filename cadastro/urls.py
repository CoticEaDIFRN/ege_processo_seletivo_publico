from django.urls import path, include
from cadastro.views import RegistrarCadastroView, Logar


urlpatterns = [
    path('registrar/', RegistrarCadastroView.as_view(), name="registrar"),
    # path('api/v1/', include(router.urls)),
    #path('admin/', admin.site.urls),
    path('index/', RegistrarCadastroView.index, name="index"),
    path('home/', Logar.home, name="home"),
    path('listar/', RegistrarCadastroView.lista_cadastros, name="listar"),
    path('entrar/', Logar.as_view(), name="login")

]
