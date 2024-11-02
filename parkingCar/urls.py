#from django.conf.urls import url 
from parkingCar import views
from django.urls import re_path 

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #url(r'^departement/$', views.departementApi),
    #url(r'^departement/([0-9]+)$', views.departementApi),

    
    
    
    #--------------------- Project Parking Car ---------------------
    
    re_path(r'^place$', views.placesApi),
    re_path(r'^place/([0-9]+)$', views.placesApi),
    re_path(r'^place/saveFile', views.saveFile),
    re_path(r'^place/reserver', views.reservePlace),
    re_path(r'^place/liberer_by_QrCode', views.libererPlaceQrCode),
    re_path(r'^place/liberer', views.libererPlace),
    
    re_path(r'^history$', views.historyApi),
    re_path(r'^history/([0-9]+)$', views.historyApi),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)