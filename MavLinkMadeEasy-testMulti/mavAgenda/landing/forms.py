from django import forms
from .models import User
from .models import UserCompleted

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'degreetrack', 'major')


class UserCompletedForm(forms.ModelForm):
    class Meta:
        model = UserCompleted
        fields = ('user', 'general_classtaken', 'core_classtaken', 'core_extension_classtaken')
