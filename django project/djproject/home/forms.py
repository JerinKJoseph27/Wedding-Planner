import re

from django import forms
from django.utils import timezone

from .models import Enqry


EVENT_CHOICES = [
    ("Wedding Venue", "Wedding Venue"),
    ("Family Makeup", "Family Makeup"),
    ("Bridal Makeup", "Bridal Makeup"),
    ("Groom Wear", "Groom Wear"),
    ("Wedding Decoration", "Wedding Decoration"),
    ("Photography & Video", "Photography & Video"),
    ("Catering", "Catering"),
    ("Jewellery", "Jewellery"),
]

class DateInput(forms.DateInput):
    input_type = 'date'

class Bookingform(forms.ModelForm):
    p_events = forms.ChoiceField(choices=EVENT_CHOICES)

    class Meta:
        model = Enqry
        fields = '__all__'

        widgets = {
            'p_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'p_email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'p_phone': forms.TextInput(attrs={'placeholder': 'Enter your contact number'}),
            'p_when': DateInput(),
            'p_events': forms.Select(),
        }

        labels = {
            'p_name' : "NAME",
            'p_email': "EMAIL",
            'p_phone' : "CONTACT NO",
            'p_when': "DATE OF EVENT",
            'p_events' : "EVENT TYPE"
        }

    def clean_p_name(self):
        name = self.cleaned_data['p_name'].strip()
        if len(name) < 2:
            raise forms.ValidationError('Name must be at least 2 characters long.')
        if not re.fullmatch(r"[A-Za-z ]+", name):
            raise forms.ValidationError('Name can contain only letters and spaces.')
        return ' '.join(name.split())

    def clean_p_email(self):
        return self.cleaned_data['p_email'].strip().lower()

    def clean_p_phone(self):
        phone = self.cleaned_data['p_phone'].strip()
        normalized_phone = re.sub(r"[^\d]", "", phone)
        if len(normalized_phone) < 10 or len(normalized_phone) > 14:
            raise forms.ValidationError('Contact number must contain between 10 and 14 digits.')
        return normalized_phone

    def clean_p_when(self):
        event_date = self.cleaned_data['p_when']
        if event_date < timezone.localdate():
            raise forms.ValidationError('Event date cannot be in the past.')
        return event_date

    def clean_p_events(self):
        event_type = self.cleaned_data['p_events']
        valid_choices = {choice[0] for choice in EVENT_CHOICES}
        if event_type not in valid_choices:
            raise forms.ValidationError('Please select a valid event type.')
        return event_type


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter username',
            'autocomplete': 'username',
        }),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'autocomplete': 'current-password',
        }),
    )


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Choose a username'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Create a password (min 8 chars)'}
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Confirm your password'}
        )

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if len(username) < 3:
            raise forms.ValidationError('Username must be at least 3 characters.')
        if not re.fullmatch(r'[A-Za-z0-9_]+', username):
            raise forms.ValidationError('Only letters, numbers, and underscores are allowed.')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email