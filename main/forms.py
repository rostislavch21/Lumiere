from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = [
            "services",
            "specialist",
            "booking_date",
            "booking_time",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "requests"
        ]

        widgets = {
            "services": forms.CheckboxSelectMultiple(),
            "specialist": forms.RadioSelect(),
            "booking_date": forms.HiddenInput(),
            "booking_time": forms.HiddenInput(),

            "first_name": forms.TextInput(attrs={
                "placeholder": "e.g. Natalia",
                "class": "form-input"
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "e.g. Krivchitska",
                "class": "form-input"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "natalia@example.com",
                "class": "form-input"
            }),
            "phone_number": forms.TextInput(attrs={
                "placeholder": "+38 (097) 602-3821",
                "class": "form-input"
            }),
            "requests": forms.Textarea(attrs={
                "rows": 4,
                "class": "form-textarea",
                "placeholder": "Any allergies or preferences we should know about?"
            }),
        }