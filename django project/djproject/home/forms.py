from django import forms
from .models import Enqry

class DateInput(forms.DateInput):
    input_type ='date'

class Bookingform(forms.ModelForm):
    class Meta:
        model = Enqry
        fields = '__all__'

        widgets = {
            'p_when' : DateInput(),
        }

        labels ={
            'p_name' : "NAME",
            'p_email': "EMAIL",
            'p_phone' : "CONTACT NO",
            'p_when':"DATE OF EVENT",
            'p_events' : "EVENT TYPE"

        }