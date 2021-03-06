from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns=[
    path('',views.index,name='index'),
    path('image/<int:id>',views.image,name='image'),
    path('search/', views.search_results, name="search_results"),
    path('uploadPhoto/', views.uploadPhoto, name="uploadPhoto"),
    path('profile/',views.profile,name='profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)