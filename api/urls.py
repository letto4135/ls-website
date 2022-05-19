from django.urls import path

from .views import *

urlpatterns = [
    path('giving', GivingData, name='giving'),
    path('services', ServiceData, name='services'),
    path('smallgroups', SmallGroupData, name='smallgroups'),
    path('staff', StaffData, name='staff'),
    path('links', LinkData, name='links')
]
