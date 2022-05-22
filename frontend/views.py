import json
import os

from sendgrid import SendGridAPIClient, ReplyTo
from sendgrid.helpers.mail import Mail
from django.shortcuts import render, redirect

from api.views import *
from .forms import PrayerRequestForm, EmailRequestForm
from .models import NewsletterRecipient, NewsletterRecipientBackup


def ContactView(request):
    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            # send email with sendgrid
            print(form.cleaned_data.get('to_ls'))
            print(form.cleaned_data.get("message"))
            message = Mail(
                from_email="info@libertystreetchurch.com",
                to_emails="info@libertystreetchurch.com",
                subject=f'Prayer Request from {form.cleaned_data.get("first_name")} {form.cleaned_data.get("last_name")}',
                html_content=f'''
                    <p>Email: {form.cleaned_data.get("inquiry_email")}</p>
                    <p>Phone: {form.cleaned_data.get("phone_number")}</p>
                    <p>Contact Method: {form.cleaned_data.get("preferred_contact_method")}</p>
                    <p>Emails can be replied to directly from here.</p>
                    <br/>
                    <p>Message: {form.cleaned_data.get("message")}</p>
                ''')
            message.reply_to = ReplyTo(
                email=form.cleaned_data.get("inquiry_email"),
                name=f'{form.cleaned_data.get("first_name")} {form.cleaned_data.get("last_name")}'
            )

            failed = 0
            while failed < 3:
                try:
                    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                    response = sg.send(message)
                    if response.status_code != 200 and response.status_code != 202:
                        print("Email failed to send", response.status_code)
                        failed += 1
                        sg.send(message)
                    else:
                        failed = 10
                except Exception as e:
                    failed += 1
                    print("Exception during email send", str(e))

            return redirect('/thanks')
    else:
        form = PrayerRequestForm()
    return render(request, 'frontend/base.html', {'form': form})


def EventsView(request):
    return render(request, 'frontend/base.html')


def GivingView(request):
    data = json.loads(GivingData(request).content.decode("UTF-8"))
    if data:
        data = data[0]
        context = {
            "id": "giving",
            "larger_text": data["larger_text"],
            "smaller_text": data["smaller_text"]
        }

        return render(request, 'frontend/base.html', context)
    else:
        return render(request, 'frontend/base.html')


def IndexView(request):
    givingdata = json.loads(GivingData(request).content.decode("UTF-8"))
    servicedata = json.loads(ServiceData(request).content.decode("UTF-8"))
    staffdata = json.loads(StaffData(request).content.decode("UTF-8"))
    links = Links(request)
    if givingdata and servicedata and links:
        data = givingdata[0]
        context = {
            "id": "giving",
            "larger_text": data["larger_text"],
            "smaller_text": data["smaller_text"],
            "servicedata": servicedata,
            "staffdata": staffdata,
            "links": links
        }
        return render(request, 'frontend/base.html', context)
    return render(request, 'frontend/base.html')


def Links(request):
    data = json.loads(LinkData(request).content.decode("UTF-8"))
    return data


def LocationView(request):
    return render(request, 'frontend/base.html')


def NewsletterView(request):
    if request.method == 'POST':
        form = EmailRequestForm(request.POST)
        if form.is_valid():
            nr = NewsletterRecipient()
            nr.email = form.cleaned_data.get('email')
            nr.first_name = form.cleaned_data.get('first_name')
            nr.last_name = form.cleaned_data.get('last_name')
            nr.save()
            nr = NewsletterRecipientBackup()
            nr.email = form.cleaned_data.get('email')
            nr.first_name = form.cleaned_data.get('first_name')
            nr.last_name = form.cleaned_data.get('last_name')
            nr.save()
            return redirect('/newsletter_thanks')
    else:
        form = EmailRequestForm()
    return render(request, 'frontend/base.html', {'form': form})


def NewsletterThanksView(request):
    return render(request, 'frontend/base.html')


def PrayerThanksView(request):
    return render(request, 'frontend/base.html')


def ServiceView(request):
    data = json.loads(ServiceData(request).content.decode("UTF-8"))
    links = Links(request)
    context = {"servicedata": data, "links": links}
    return render(request, 'frontend/base.html', context)


def SmallGroupView(request):
    data = json.loads(SmallGroupData(request).content.decode("UTF-8"))
    context = {"groups": data}
    return render(request, 'frontend/base.html', context)


def StaffView(request):
    data = json.loads(StaffData(request).content.decode("UTF-8"))
    context = {"staffdata": data}
    return render(request, 'frontend/base.html', context)
