
from django.contrib import admin
from django.urls import path , include
from chat.views import index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/' , include('chat.urls' , namespace='chat'))
]

from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)