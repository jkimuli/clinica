from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    
    #path('grappelli/', include('grappelli.urls')), # grappelli URLS
    #path('jet/',include('jet.urls',namespace='jet')),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('clinic/',include('clinic.urls')),
    path('sales/',include('sales.urls')),
    path('expenses/',include('expenditure.urls')),
    path('assets/',include('assets.urls')),

]
    


    
    