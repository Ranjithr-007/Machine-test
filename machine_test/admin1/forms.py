from django import forms
from user.models import *


class AdForm(forms.ModelForm):
   class Meta:
       model = Employee
       fields = ('name',
                 'age',
                 'department')