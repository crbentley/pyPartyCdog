from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'degreetrack', 'major', 'general_classtaken', 'core_classtaken', 'core_extension_classtaken')
