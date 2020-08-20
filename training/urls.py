from django.urls import path  # path is a relative path to create a route
from django.conf import settings
# static provides a file static to me
from django.conf.urls.static import static
from django.conf.urls import url
from training import views


urlpatterns = [
    path('api/training/', views.training_list),
    path('api/training/<int:id>/', views.training_detail),
    path('api/entity/', views.entity_list),
    path('api/entity/<int:id>', views.entity_detail),
    path('api/instruct/', views.instructor_list),
    path('api/instruct/<int:id>/', views.instructor_detail),
    path('api/event/', views.event_list),
    path('api/event/<int:id>/', views.event_detail),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
