from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('personajes/', views.personajes, name='personajes'),
    path('acerca/', views.acerca, name='acerca'),
    path('noticias/', views.noticias, name='noticias'),
    path('offline/', views.offline, name='offline'),
path('serviceworker.js', views.serviceworker, name='serviceworker'),
    path('manifest.json', views.manifest, name='manifest'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
