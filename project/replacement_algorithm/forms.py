from django import forms

ALOGORITHM_CHOICES = [
    ('FIFO', 'FIRST IN FIRST OUT'),     # first in first out
    ('LRU', 'LEAST RECENTLY USED'),     # least recently used
    ('LFU', 'LEAST FREQUENTLY USED'),   # least frequently used
    ('MFU', 'MOST FREQUENTLY USED'),    # most frequently used
]
    
class AlgorithmForm(forms.Form):
    numbers = forms.CharField(label='Numbers', max_length=100)
    algorithm = forms.CharField(label='Algorithm', widget=forms.Select(choices=ALOGORITHM_CHOICES))