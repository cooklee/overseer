from django import forms
from django.core.exceptions import ValidationError

from tracker.models import Task, Cost


def check_amount(value):
    if value < 5:
        raise ValidationError("no wysil sie troszkę bardziej")

def liczby_podzielne_przez2(value):
    if value %2 == 1:
        raise ValidationError("oj nieszczescie")

class AddTimeSpentToTaskForm(forms.Form):
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),
                                validators=[check_amount, liczby_podzielne_przez2])
    task = forms.ModelChoiceField(queryset=Task.objects.all(),
                                  widget=forms.Select(attrs={'class':'form-control'}))
    date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control',
                                      'type':'date'})
    )

    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['task'].done:
            raise ValidationError('zadanie juz zakonczone nie mozna dodawać czasu spędzonego do tego zadania')


class AddCostToTaskForm(forms.ModelForm):
    class Meta:
        model = Cost
        # fields = ['description', 'amount']
        exclude = ['task']
        #fields = '__all__'


