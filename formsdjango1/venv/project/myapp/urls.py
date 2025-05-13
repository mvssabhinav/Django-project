from django.urls import path
from .views import eventform,birthday,marriage,home,about,Login,success,Login2,retrieved,staffRetrivedData,logout_view,welcomepage,delete_event,delete_birthday,delete_marriage,proceed_event

urlpatterns = [
    path('',home,name='home'),  
    path('about',about,name='about'),
    path('eventform',eventform,name="eventform"),
    path('birthday',birthday,name='birthday'),
    path('marriage',marriage,name='marriage'),
    path('Login',Login,name='Login'),
    path('Login2',Login2,name='Login2'),
    path('retrieved',retrieved,name='retrieved'),
    path('staffRetrivedData',staffRetrivedData,name='staffRetrivedData'),
    path('success',success,name='success'),
    path('logout',logout_view,name='logout'),
    path('welcomepage',welcomepage,name='welcomepage'),
    path('delete_event/<int:id>/', delete_event, name='delete_event'),
    path('delete_birthday/<int:id>/', delete_birthday, name='delete_birthday'),
    path('delete_marriage/<int:id>/', delete_marriage, name='delete_marriage'),
    path('proceed/<int:event_id>/', proceed_event, name='proceed_event')

]