from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin

from inscricao import views

app_name = 'ege_selecao'
urlpatterns = [
    path('', views.nova_inscricao, name='nova_inscricao'),
    # path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls)
]
