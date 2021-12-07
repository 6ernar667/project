from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    # path('mountains/', include('mountains.urls')),
    # path('sportshops/', include('sportshops.urls')),
]
