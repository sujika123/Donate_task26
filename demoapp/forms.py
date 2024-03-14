from django import forms
from django.contrib.auth.forms import UserCreationForm

from demoapp.models import Login, user, donmngmt, recipient, branchmngmt, donation, requestdonation


class loginform(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class userloginform(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'
        exclude = ('user',)

class donmngmtloginform(forms.ModelForm):
    class Meta:
        model = donmngmt
        fields = '__all__'
        exclude = ('user',)

class recipientloginform(forms.ModelForm):
    class Meta:
        model = recipient
        fields = '__all__'
        exclude = ('user','status')

class branchloginform(forms.ModelForm):
    class Meta:
        model = branchmngmt
        fields = '__all__'
        exclude = ('user','status')


class donationform(forms.ModelForm):
    class Meta:
        model = donation
        fields = '__all__'
        exclude = ('user','status')


class requestdonationform(forms.ModelForm):
    class Meta:
        model = requestdonation
        fields = '__all__'
        exclude = ('user','status')
