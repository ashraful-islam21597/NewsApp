from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('Fullname','username','email',)
        #fields = UserCreationForm.Meta.fields +('Profilepicture',)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('Fullname','username', 'email',)
        #fields = UserChangeForm.Meta.fields