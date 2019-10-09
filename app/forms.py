from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Post, Prof
from django.contrib.auth.forms import AuthenticationForm


# 登録フォーム
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'acctype', 'acctext')  # formの項目設定
        labels = {
            'acctype': 'アカウントの種類',
        }  # ラベル名の設定


# 投稿フォーム
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)


class ProfForm(forms.ModelForm):
    class Meta:
        model = Prof
        fields = ('icon',)
