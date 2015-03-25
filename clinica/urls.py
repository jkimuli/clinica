from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clinica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),

    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login'}),

    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^clinic/',include('clinic.urls')),
    url(r'^sales/',include('sales.urls')),
    url(r'^expenses/',include('expenditure.urls')),
    url(r'^assets/',include('assets.urls')),
    url(r'^grappelli',include('grappelli.urls')),

)
