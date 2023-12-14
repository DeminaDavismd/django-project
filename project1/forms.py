from django import forms
from .models  import appointmet

class DateInput(forms.DateInput):
    input_type ='date'

class appointmetForms(forms.ModelForm):
    class Meta:
        model=appointmet
        fields='__all__'

        widgets = {
            'booked_date': DateInput(),
        }
        labels={
          'name':"Patient Name",
          'phone':"Patient Phone",
           'email':"Patient Email",
           'doc_name':"Doctor Name",
            'booked_date':"Booking Date",
        }