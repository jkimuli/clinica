from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', include('pages.urls')),   
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('clinic/',include('clinic.urls')),
    path('expenses/',include('expenditure.urls')),
    path('assets/',include('assets.urls')),
    path('pharmacy/',include('pharmacy.urls')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    


    
    