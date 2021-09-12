from core.models import Contact
from django import forms

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['fullname','email','phone','text']


        widgets = {
            'fullname':forms.TextInput(attrs={'class':'form-control','placeholder':'Ad'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Ünvanı'}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Telefon'}),
            'text':forms.Textarea(attrs={'class':'form-control','placeholder':'Mətn','rows':'2'}),
        }