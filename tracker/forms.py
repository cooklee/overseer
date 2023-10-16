from django import forms

from tracker.models import Task


class AddTimeSpentToTaskForm(forms.Form):
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    task = forms.ModelChoiceField(queryset=Task.objects.all(),
                                  widget=forms.Select(attrs={'class':'form-control'}))
    date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )