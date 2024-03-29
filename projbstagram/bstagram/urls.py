from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include
import photo .views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')),
    path('accounts/', include('accounts.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)