from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm

#登録フォーム
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'acctype','acctext') #formの項目設定
