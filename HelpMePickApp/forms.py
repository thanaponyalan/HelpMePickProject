from django import forms

class ActivityForm(forms.Form):
    ageRange=forms.IntegerField()
    actType=forms.IntegerField()