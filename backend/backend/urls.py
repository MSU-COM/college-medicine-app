# Main project urls

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from home.urls import home_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/home/', include(home_router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)