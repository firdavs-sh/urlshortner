from django.contrib import admin
from django.urls import path,include
from django.urls import path
from django.views.generic import RedirectView
from Home.views import download_video
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('us/', include('myapp.urls')),
    path("",include("main.urls")),
    path('yd/', download_video,name="yd"),
    path("bg/",include("bgremove.urls")),
    path('<string>', RedirectView.as_view(url='/')) 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
