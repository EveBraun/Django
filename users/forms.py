from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput, 
                               error_messages={'required':'Not empty!'})
    password2 = forms.CharField(label='Password once more', 
                               widget=forms.PasswordInput)
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords are different!')
        return cd('password2')


    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'first_name', 'email')
        help_texts = {'username': 'Only letters and symbols'}
        verbose_name = {'username': 'login'}
        labels = {
            'username': 'login',
            'first_name': 'name',

        }
        widgets = {
            'username': forms.TextInput,
        }
