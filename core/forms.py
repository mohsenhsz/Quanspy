form django.form import forms

class UserUploadForm(forms.Form):
    up_file = forms.File