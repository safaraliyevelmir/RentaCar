from django import forms
from django.forms import widgets
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'titul',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'message',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'from_place',
            'to_place',

            'is_wifi',
            'to_airplane',
            'in_city',
            'has_wifi',
            'child_seat',
            ]
        
        widgets = {
            'titul':forms.Select(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control','rows':'2'}),

            'start_date':forms.TextInput(attrs={'class':'form-control',"id":"datepickerPickUpDate"}),
            'start_time':forms.TextInput(attrs={'class':'form-control',"id":"datepickerPickUpTime"}),

            'end_date':forms.TextInput(attrs={'class':'form-control',"id":"datepickerDropOffDate"}),
            'end_time':forms.TextInput(attrs={'class':'form-control',"id":"datepickerDropOffTime"}),

            'from_place':forms.Select(attrs={'class':'form-control'}),
            'to_place':forms.Select(attrs={'class':'form-control'}),

            'is_wifi':forms.CheckboxInput(attrs={'class':'owncheckbox'}),
            'to_airplane':forms.CheckboxInput(attrs={'class':'owncheckbox'}),
            'in_city':forms.CheckboxInput(attrs={'class':'owncheckbox'}),
            'has_wifi':forms.CheckboxInput(attrs={'class':'owncheckbox'}),
            'child_seat':forms.CheckboxInput(attrs={'class':'owncheckbox'}),
        }
    



        