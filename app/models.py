from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

#ユーザー
class User(AbstractUser):
    TYPE_CHOICES = (('company','企業アカウント'),
                    ('general','一般アカウント'))

    acctype = models.CharField(choices=TYPE_CHOICES,max_length=100,default='general')
    acctext = models.TextField(blank=True,max_length=1000)
    icon = models.ImageField(
        upload_to='img',
        verbose_name='icon',
        blank=True,
    )

#投稿
class Post(models.Model):
    CAT_CHOICES = (('finace','金融'),
                   ('it_cat','IT'),
                   ('media','メディア'),
                   ('machine','自動車・機械'),
                   ('retail','小売'),
                   ('service','サービス'),
                   ('arc','建築・不動産'),
                   ('energy','エネルギー・資源'),
                   ('preci','電気・精密'),
                   ('life','生活関連'),
                   ('fanda','飲食'),
                   ('logi','物流'),
                   ('food','食品'),
                   ('cloth','衣料'),
                   ('enta','娯楽'),)

    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=1000)
    category = models.CharField(choices=CAT_CHOICES,max_length=100,default='general')
    product_img = models.ImageField(
        upload_to='img',
        verbose_name='product',
        blank=False,
    )
    #fav = models.ForeignKey(??, on_delete=models.CASCADE) #ふぁぼ機能、実装予定
    #category = models.ForeignKey(User, on_delete=models.CASCADE)


#ユーザーに紐づけられるプロフィール
class Prof(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #category = models.ForeignKey(User, on_delete=models.CASCADE)
    icon = models.ImageField(
        upload_to='img/',
        blank=True,
    )


#カテゴリ
'''
class Category(models.Model):
    TYPE_CHOICES = (タプル)

'''