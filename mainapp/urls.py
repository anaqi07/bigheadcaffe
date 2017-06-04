from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^createcoffee/$', createCoffee, name='createcoffee'),
    url(r'^editcoffee/(?P<coffee_id>[0-9]+)/$', editCoffee, name='editcoffee'),

    url(r'^createbean/$', createBean, name='createbean'),
    url(r'^editbean/(?P<bean_id>[0-9]+)/$', editBean, name='editbean'),
    url(r'^deletebean/(?P<bean_id>[0-9]+)/$', deleteBean, name='deletebean'),

    url(r'^createroast/$', createRoast, name='createroast'),
    url(r'^editroast/(?P<roast_id>[0-9]+)/$', editRoast, name='editroast'),
    url(r'^deleteroast/(?P<roast_id>[0-9]+)/$', deleteRoast, name='deleteroast'),

    url(r'^createpowder/$', createPowder, name='createpowder'),
    url(r'^editpowder/(?P<powder_id>[0-9]+)/$', editPowder, name='editpowder'),
    url(r'^deletepowder/(?P<powder_id>[0-9]+)/$', deletePowder, name='deletepowder'),

    url(r'^createsyrup/$', createSyrup, name='createsyrup'),
    url(r'^editsyrup/(?P<syrup_id>[0-9]+)/$', editSyrup, name='editsyrup'),

    url(r'^createorder/(?P<coffee_id>[0-9]+)/$', createOrder, name='createorder'),

]
