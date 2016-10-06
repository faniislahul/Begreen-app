"""
Definition of urls for ASME_C.
"""

from django.views.generic.base import RedirectView
from django.conf.urls import include, url
from core import views, controller, abcmodule
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [

    url(r'^$', views.Home , name='home'),
    url(r'^settings/', views.settings, name = 'settings'),
    url(r'^pengeluaran/', views.pengeluaran, name = 'pengeluaran'),
    url(r'^pengeluaran_response/', controller.response_pengeluaran, name = 'pengeluaran_response'),
    url(r'^persediaan/', views.persediaan, name = 'persediaan'),
    url(r'^persediaan_response/', controller.response_persediaan, name = 'persediaan_response'),    
    url(r'^pemasukan/', views.pemasukan, name = 'pemasukan'),
    url(r'^pemasukan_response/', controller.response_pemasukan, name = 'pemasukan_response'), 
    url(r'^produk/', views.produk, name = 'produk'),
    url(r'^produk_response/', controller.response_produk, name = 'produk_response'),
    
    url(r'^abc_calculate/', abcmodule.calculate, name = 'abc_calculate'),
    
    url(r'^akunlv1_list/$', views.Akunlv1.as_view(), name = 'akunl1_list'),
    url(r'^akunlv2_list/$', views.Akunlv2.as_view(), name = 'akunl2_list'),
    url(r'^akunlv3_list/$', views.Akunlv3.as_view(), name = 'akunl3_list'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
