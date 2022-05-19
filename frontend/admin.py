import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import *


class ExportCsvMixin:
    def export_for_email(self, request, queryset):
        meta = self.model._meta
        field_names = ["email"]
        response = HttpResponse(content_type='text')
        response['Content-Disposition'] = 'attachment; filename={}.txt'.format(str(meta).replace('frontend.', '') + "emails")

        row = ""
        for obj in queryset:
            row += f"{getattr(obj, field_names[0])}; "
        response.write(row[:-2])

        return response

    def export_data(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        print(field_names)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(str(meta).replace('frontend.', ''))
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_for_email.short_description = "Export Selected For Email"
    export_data.short_description = "Export All Data"


class NewsletterAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('first_name', 'last_name', 'email')
    actions = ["export_for_email", 'export_data']


class NewsletterBackupAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('first_name', 'last_name', 'email')
    actions = ["export_for_email", 'export_data']


admin.site.register(NewsletterRecipient, NewsletterAdmin)
admin.site.register(NewsletterRecipientBackup, NewsletterAdmin)
