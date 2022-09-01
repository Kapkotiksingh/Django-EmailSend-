from email import message
from socket import fromshare
from django import forms

class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)
