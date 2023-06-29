from django import forms

    
class AlgorithmForm(forms.Form):
    numbers = forms.CharField(label='Numbers', max_length=100)
