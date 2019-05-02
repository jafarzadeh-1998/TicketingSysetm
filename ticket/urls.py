from django.urls import path 
from django.conf.urls import url

from . import views


app_name = 'ticket'
urlpatterns = [
   path('', views.Index.as_view(),name="home"),
   path('login/',views.MyLogin ,name='login'),
   path('logout/',views.MyLogout ,name='logout'),
   path('signup',views.signup ,name='signup'),
   path('create_ticket' ,views.CreateTicket.as_view() ,name='new-ticket'),
   path('ticket_list',views.TicketList.as_view() ,name="ticket-list"),
   url(r'^detail/(?P<pk>[-\d]+)/$' ,views.TicketDetail.as_view() ,name ='ticket-detail'),
   url(r'^create_message/(?P<pk>[-\d]+)/$' ,views.CreateMessage.as_view() ,name ='new_message'),
   path('reply_list' ,views.ReplyList.as_view() ,name='reply-list'),
   url(r'^reply/(?P<pk>[-\d]+)/$' ,views.Reply.as_view() ,name ='reply'),
]
