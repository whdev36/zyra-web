from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='Username',
        label_suffix=' *',
        help_text='Your unique username to log in.',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'autofocus': True
        })
    )

    password = forms.CharField(
        min_length=8,
        label='Password',
        label_suffix=' *',
        help_text='Make sure your password is correct.',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )

    remember_me = forms.BooleanField(
        required=False,
        label='Remember me',
        label_suffix=' *',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if len(username.strip()) < 3:
            raise forms.ValidationError('Username must be at least 3 characters long.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if password and len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters.')
        return password
