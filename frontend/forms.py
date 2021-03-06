from django import forms
from captcha.fields import CaptchaField


attrs = {
    "class": "form-control"
}


class PrayerRequestForm(forms.Form):
    first_name = forms.CharField(max_length=50, min_length=2, widget=forms.TextInput(attrs=attrs))
    last_name = forms.CharField(max_length=50, min_length=2, widget=forms.TextInput(attrs=attrs))
    inquiry_email = forms.EmailField(required=False, label="Email", widget=forms.EmailInput(attrs=attrs))
    phone_attrs = attrs.copy()
    phone_attrs["type"] = "tel"
    phone_attrs["pattern"] = "[0-9]{3}-[0-9]{3}-[0-9]{4}|[0-9]{10}"
    phone_number = forms.CharField(
        help_text="Format: 1234567890",
        required=False,
        label='Phone number',
        max_length=10,
        widget=forms.TextInput(attrs=phone_attrs)
    )
    preferred_contact_method = forms.ChoiceField(
        choices=[("none", "None"), ("email", "Email"), ("phone", "Phone")],
        widget=forms.Select(attrs=attrs)
    )
    message = forms.CharField(label="Message", min_length=5, widget=forms.Textarea(attrs=attrs))
    captcha = CaptchaField()


class EmailRequestForm(forms.Form):
    first_name = forms.CharField(max_length=50, min_length=2, widget=forms.TextInput(attrs=attrs))
    last_name = forms.CharField(max_length=50, min_length=2, widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs=attrs))
    captcha = CaptchaField()
