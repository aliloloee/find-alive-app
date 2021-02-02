from django.urls import path
from .import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('post-coordinate', views.CoordinateViewSet)


urlpatterns = [
    path('post-user', views.create_user),
    path('give-token', views.CustomAuthToken.as_view()),
    path('get-all-coordinates', views.get_all_coordinates),
    path('get-final-coords', views.get_final_coordinates),
]


urlpatterns += router.urls