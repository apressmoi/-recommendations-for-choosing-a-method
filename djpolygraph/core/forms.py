from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'exampleInputUsername',
            'placeholder': 'Введите имя пользователя'
        }   
    ), label="Имя пользователя")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'exampleInputPassword1',
            'placeholder': 'Введите пароль'
        }
    ), label="Пароль")

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Данного пользователя не существует')
            if not user.check_password(password):
                raise forms.ValidationError('Проверьте правильность введеного пароля')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Адресс электронной почты',
        widget=forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'id': 'exampleInputEmail1',
                    'placeholder': 'Введите адресс электронной почты'
                })
    )
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'exampleInputPassword1',
            'placeholder': 'Введите пароль'
        }
    ), label='Пароль')

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'exampleInputPassword1',
            'placeholder': 'Введите пароль'
        }
    ), label='Потверджение пароля')

    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'id': 'exampleInputUsername',
                        'placeholder': 'Введите имя'
                    })
            )
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'exampleInputUsername',
            'placeholder': 'Введите фамилию'
        }
    ))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'exampleInputUsername',
            'placeholder': 'Введите имя пользователя'
        }
    ))

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
        ]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2', 'email']:
            self.fields[fieldname].help_text = None

    def clean_password(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password')
        if len(password1) < 8:
            raise forms.ValidationError('Пароль должен содержать 8 или более символов')
        return password1

    def clean_password2(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Введеные пароли не совпадают')
        return password2
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_query = User.objects.filter(email=email)
        if email_query.exists():
            raise forms.ValidationError('Такой адресс электронной почты уже существует')
        return email

