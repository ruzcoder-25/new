from django import forms
# from django.contrib.auth.models import User

from account.models import CustomUser, Transaction


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'password',
        ]


    def save(self, commit=True):
        return CustomUser.objects.create_user(
            username=self.cleaned_data.get('username'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            phone_number=self.cleaned_data.get('phone_number'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password'),

        )

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = (
            'from_user',
            'to_user',
            'amount',
        )