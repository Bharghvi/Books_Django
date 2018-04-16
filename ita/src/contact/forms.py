from django import forms

class contactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, help_text="100 Max Chars")
    email = forms.EmailField(required=True)
    category = forms.CharField(required=True, max_length=100)
    comment = forms.CharField(required=True, widget=forms.Textarea)
