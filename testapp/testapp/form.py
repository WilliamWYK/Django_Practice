from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 15, min_length=8)
    password = forms.CharField(max_length = 20, min_length=8)

    def clean_password(self):
        password = self.cleaned_data['password']
        if ' ' in password:
            raise forms.ValidationError('不可使用空白')
        
        return password
    