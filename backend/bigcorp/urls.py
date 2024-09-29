from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
#rom django_email_verification import urls as email_urls

#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls', namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)