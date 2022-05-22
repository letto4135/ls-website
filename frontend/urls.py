from django.urls import path, include

from .views import *

urlpatterns = [
    path('captcha/', include('captcha.urls')),
    path('contact', ContactView, name='contact'),
    path('events', EventsView, name='events'),
    path('', IndexView, name='index'),
    path('giving', GivingView, name='giving'),
    path('location', LocationView, name='location'),
    path('newsletter', NewsletterView, name='newsletter'),
    path('newsletter_thanks', NewsletterThanksView, name='newsletter_thanks'),
    path('thanks', PrayerThanksView, name='thanks'),
    path('times', ServiceView, name='services'),
    path('groups', SmallGroupView, name='smallgroups'),
    path('staff', StaffView, name='staff'),
]
