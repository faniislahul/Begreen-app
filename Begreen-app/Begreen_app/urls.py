"""
Definition of urls for Begreen_app.
"""

from django.conf.urls import include, url
from webapp import views, webadmin
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^categories/', views.categories, name='categories'),
    url(r'^products/', views.products, name='products'),
    
    #cust admin section
    url(r'^admin_dash/', webadmin.dash, name='admin_dash'),
    url(r'^admin_products/', webadmin.products_admin, name='admin_products'),
    url(r'^admin_categories/', webadmin.categories_admin, name='admin_categories'),
    
    #handler
     url(r'^crudhandler/', webadmin.crudhandler, name='crudhandler'),

    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
