from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from orders import urls as order_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'', include((order_urls,'order_urls' ) , namespace = 'orderurls') ),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
