from django import forms
from . models import Subscribers


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', ]
