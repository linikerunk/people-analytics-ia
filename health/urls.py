from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from health import views
import requests

app_name = "health"


urlpatterns = [
    # path('api/health/', views.health_list),
    # path('api/health/<int:id>', views.health_detail),
    path('api/doctor_certification/', views.DoctorCetification.as_view(),
    name='doctor_certification'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
