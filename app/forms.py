from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    UsernameField, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import CustomerDetails, CustomerAddress, Town
import datetime
from dateutil.relativedelta import relativedelta
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model =User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class DateInput(forms.DateInput):
    input_type = 'date'
    min = datetime.datetime.today() - relativedelta(years=35)
    max = datetime.datetime.today() - relativedelta(years=12)


class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = CustomerAddress
        fields = ['county', 'town', 'pick_up_station', 'zip_code', 'contact']

        widgets = {
            'county': forms.Select(attrs={'class': 'form-control'}),
            'town': forms.Select(attrs={'class': 'form-control'}),
            'pick_up_station': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['town'].queryset = Town.objects.none()

        if 'county' in self.data:
            try:
                county_id = int(self.data.get('county'))
                self.fields['town'].queryset = Town.objects.filter(county__id=county_id).order_by('town')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['town'].queryset = self.instance.county.town_set.order_by('town')


class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ['first_name', 'last_name', 'gender', 'next_of_kin', 'next_of_kin_contact',
                  'date_of_birth', 'contact', 'sub_county', 'school', 'games_of_interest',
                  'height_in_cm', 'weight_in_kgs', 'special_needs']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'next_of_kin': forms.Select(attrs={'class': 'form-control'}),
            'next_of_kin_contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'sub_county': forms.Select(attrs={'class': 'form-control'}),
            'school': forms.TextInput(attrs={'class': 'form-control'}),
            'games_of_interest': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'height_in_cm': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight_in_kgs': forms.NumberInput(attrs={'class': 'form-control'}),
            'special_needs': forms.Select(attrs={'class': 'form-control'})

        }


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={
        'autofocus': 'True', 'autocomplete': 'current-password', 'class': 'form-control'
    }))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={
        'autocomplete': 'current-password', 'class': 'form-control'
    }))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'autocomplete': 'current-password', 'class': 'form-control'
    }))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


class MyPasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={
        'autocomplete': 'current-password', 'class': 'form-control'
    }))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'autocomplete': 'current-password', 'class': 'form-control'
    }))


