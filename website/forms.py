from django import forms
from website.models import Contact, NewsLetter
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(max_length=255)
    
class ConatctForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields ='__all__'

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields ='__all__'