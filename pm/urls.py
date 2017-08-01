from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^inventory/index', views.inventory_index, name='inventory_index'),
    url(r'^inventory/(?P<item_id>[0-9]+)/$', views.inventory_detail, name='inventory_detail'),
    url(r'^inventory/new', views.inventory_new, name='new'),
]
