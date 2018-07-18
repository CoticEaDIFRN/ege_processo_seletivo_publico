from django.contrib import admin
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('%s/admin/' % settings.URL_PREFIX, admin.site.urls),
]
