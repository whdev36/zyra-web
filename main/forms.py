from django import forms
from django.utils.safestring import mark_safe
from django.template.defaultfilters import yesno

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=150,
        widget=forms.TextInput()
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput()
    )
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['autofocus'] = True
        self.fields['username'].help_text = 'Enter the username you registered with.'
        self.fields['username'].error_messages = {
            'required': 'Please enter your username.',
            'max_length': 'Your username is too long. Please keep it under 150 characters.',
            'min_length': 'Username must be at least 3 characters long.'
        }

        self.fields['password'].help_text = 'Make sure your password is correct and secure.'
        self.fields['password'].error_messages = {
            'required': 'Please enter your password.',
            'min_length': 'Password must be at least 8 characters long.'
        }

        fields_config = {
            'username': {
                'widget_class': 'form-control',
                'placeholder': 'Enter your username',
                'label': 'Username'
            },
            'password': {
                'widget_class': 'form-control',
                'placeholder': 'Enter your password',
                'label': 'Password'
            },
            'remember_me': {
                'widget_class': 'form-check-input',
                'label': 'Remember me'
            }
        }

        for field_name, config in fields_config.items():
            field = self.fields[field_name]
            field.widget.attrs['class'] = config['widget_class']
            field.label = config['label']
            field.label_suffix = ' *' if field_name != 'remember_me' else ''
            if 'placeholder' in config:
                field.widget.attrs['placeholder'] = config['placeholder']

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

    def as_div(self):
        return mark_safe(
            '\n'.join(
                f'''
                <div class="form-group mb-3">
                    {field.label_tag(attrs={"class": "form-label"})}
                    {field}
                    <small class="text-muted">{field.help_text}</small>
                    {''.join(f'<div class="text-danger">{error}</div>' for error in field.errors)}
                </div>
                ''' if not field.is_hidden and field.name != 'remember_me' else
                # Special case for 'remember_me' checkbox
                f'''
                <div class="form-check mb-5">
                    {field}  <!-- Use the field widget for the checkbox -->
                    <label class="form-check-label" for="remember_me">{field.label}</label>
                    {''.join(f'<div class="text-danger">{error}</div>' for error in field.errors)}
                </div>
                '''
                for field in self
            )
        )