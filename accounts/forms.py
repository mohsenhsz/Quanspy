from django import forms


class UserRegisterationForm(forms.Form):
    form_class = 'form-control'
    username = forms.CharField(widget=forms.TextInput(attrs={'class':form_class}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':form_class}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':form_class}))