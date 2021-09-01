from django import forms
from . models import Subscribers, SubscriberEmail


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', ]


class EmailForm(forms.ModelForm):
    class Meta:
        model = SubscriberEmail
        fields = '__all__'