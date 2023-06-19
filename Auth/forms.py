from django import forms


class LoginForm(forms.Form):
    Username = forms.CharField(label="Username", max_length=100, strip=True)
    Password = forms.CharField(label="Password", widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    FirstName = forms.CharField(label='First Name', max_length=100, strip=True)
    LastName = forms.CharField(label='Last Name', max_length=100, strip=True)
    EmailId = forms.EmailField(label='Email')
    UserId = forms.CharField(label='UserId', strip=True)
    Password = forms.CharField(label='Password', widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
