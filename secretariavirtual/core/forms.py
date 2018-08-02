from django import forms

class LoginForm(forms.Form):

    login = forms.CharField(
    	max_length=20,
        label=("Login"),
        help_text=("Login")
    )
    password = forms.CharField(
    	max_length=20,
        label=("Senha"),
        help_text=("Senha"),
    	widget=forms.PasswordInput
    )