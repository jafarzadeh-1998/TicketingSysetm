from django.urls import path 
from django.conf.urls import url

from . import views


app_name = 'ticket'
urlpatterns = [
   path('', views.loginu,name="login"),
   path('signup',views.signin),
   # path('dashboard',views.dashboard),
   path('dashboard',views.TicketList.as_view() ,name="ticket-list"),
   url(r'^detail/(?P<pk>[-\d]+)/$' ,views.TicketDetail.as_view() ,name ='ticket-detail'),
   url(r'^insert/(?P<pk>[-\d]+)/$' ,views.createMassage ,name ='insert'),
]
