import views
from django.contrib import admin
from django.urls import path,include

from personal.views import (
    home,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('personal.urls')),


]





