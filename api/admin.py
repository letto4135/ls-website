from django.contrib import admin
from api.models import *


class GivingAdmin(admin.ModelAdmin):
    list_display = ('larger_text', 'smaller_text')


class LinkAdmin(admin.ModelAdmin):
    list_display = ('link_name', 'service')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('text',)


class SmallGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'led_by', 'location', 'when')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')


admin.site.register(Giving, GivingAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SmallGroup, SmallGroupAdmin)
admin.site.register(Staff, StaffAdmin)
