from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from users import views

app_name = "health"


urlpatterns = [
    path('api/health/', views.employee_list),
    path('api/health/<int:id>', views.employee_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
