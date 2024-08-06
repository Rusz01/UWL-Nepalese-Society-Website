from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    number = forms.CharField(max_length=11, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'style': 'height: 200px'}), required=True)

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if not number.isdigit() or len(number) != 11:
            raise forms.ValidationError("Please enter a valid 10-digit phone number.")
        return number
