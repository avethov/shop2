"""
Definition of urls for shop2.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from apps.example.forms import BootstrapAuthenticationForm

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'apps.example.views.home', name='home'),
    url(r'^contact$', 'apps.example.views.contact', name='contact'),
    url(r'^about', 'apps.example.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'apps.example/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'apps.catalogue.views.index', name='index'),
    url(r'^list1/', include('apps.catalogue.urls')),
    url(r'^list2/', 'apps.catalogue.views.Product2View', name='Product2View'),
)