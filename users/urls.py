from django.urls import path # path is a relative path to create a route
from django.conf.urls.static import static # static provides a file static to me
from django.conf import settings

from users.views import UserProfileView


urlpatterns = [
    path('', UserProfileView.as_view(), name='user_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
