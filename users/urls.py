from django.urls import path # path is a relative path to create a route
from django.conf import settings
from django.conf.urls.static import static # static provides a file static to me
from django.conf.urls import url
from users import views


urlpatterns = [
    url(r'^api/employees/$', views.employee_list),
    url(r'^api/employees/(?P<pk>[0-9]+)$', views.employee_detail),
    url(r'^api/costcenter/$', views.employee_list),
    url(r'^api/costcenter/(?P<pk>[0-9]+)$', views.employee_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
