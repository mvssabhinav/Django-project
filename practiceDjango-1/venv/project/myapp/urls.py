from django.urls import path
from.views import home, retrived
urlpatterns=[
    path('',home,name='home'),
    path('retrived',retrived,name='retrived')
]