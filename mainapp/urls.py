from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'user_list/$', user_list, name='user_list'),
    url(r'^user_coffees/(?P<user_id>[0-9]+)/$', user_coffees, name='user_coffees'),
    url(r'^send_order_email/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$', send_order_email, name='send_order_email'),
    url(r'^replicate_order/(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})/$', replicate_order, name='replicate_order'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^naughty_page/$', naughty_page, name='naughty_page'),

    url(r'^createcoffee/$', createCoffee, name='createcoffee'),
    url(r'^editcoffee/(?P<coffee_id>[0-9]+)/$', editCoffee, name='editcoffee'),
    url(r'^deletecoffee/(?P<coffee_id>[0-9]+)/$', deleteCoffee, name='deletecoffee'),

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
#gggg
