from django import forms
from .models import Profile

class RegisterForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'firstname',
            'surname',
            'fathersname',
            'address',
            'job',
            'phone',
            'email',
            'avatar',
        )