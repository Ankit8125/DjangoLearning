from django import forms
from .models import ChaiVariety

class ChaiVarietyForm(forms.Form): # All forms are linked on basis on model
  chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label="select chai variety") # It can query in our existing model
  # This ModelChoiceField is intelligent. It will automatically know which one is in dropdown format
  