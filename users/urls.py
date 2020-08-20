from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from users import views

app_name = "users"


urlpatterns = [
    path('', views.index, name="index"),
    path('api/employees/', views.employee_list),
    path('api/employees/<int:id>', views.employee_detail),
    path('api/costcenter/', views.employee_list),
    path('api/costcenter/<int:id>', views.employee_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
