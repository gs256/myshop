from django.contrib import admin
from apps import home
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls'))
]
