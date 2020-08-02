from django import forms

class BGVForm(forms.Form):
    CID = forms.CharField(label = 'CID', max_length=100)
    GRVM = forms.CharField(label = 'GRVM', max_length=100)