from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('', include('users.urls')),
    path('token-auth/', obtain_jwt_token),
    path('painel/', admin.site.urls)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# How there's no media server to give  static files, I'm get own my root as
# default of machine
