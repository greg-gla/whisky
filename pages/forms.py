from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=32, widget=forms.PasswordInput(attrs={'class': 'form'
                                                                                                            '-control'}))
    password2 = forms.CharField(label="Repeat_Password", max_length=32,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
