from rest_framework.authtoken import views as auth_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('find-alive-api/', include('myApp.urls')),
    # path('api-token-auth', auth_views.obtain_auth_token),
    path('api-auth', include('rest_framework.urls')),
]