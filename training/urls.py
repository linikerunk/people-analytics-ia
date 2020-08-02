from django.urls import path  # path is a relative path to create a route
from django.conf import settings
# static provides a file static to me
from django.conf.urls.static import static
from django.conf.urls import url
from users import views


urlpatterns = [
    url(r'^api/training/$', views.training_list),
    url(r'^api/training/(?P<pk>[0-9]+)$', views.training_detail),
    url(r'^api/entity/$', views.entity_list),
    url(r'^api/entity/(?P<pk>[0-9]+)$', views.entity_detail),
    url(r'^api/instruct/$', views.instruct_list),
    url(r'^api/instruct/(?P<pk>[0-9]+)$', views.instruct_detail),
    url(r'^api/event/$', views.event_list),
    url(r'^api/event/(?P<pk>[0-9]+)$', views.event_detail),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
