from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from posts.models import Post


# AbstractUser: Djangoが用意しているUserモデルを継承する
class User(AbstractUser):
    # アイコンを画像を保存できるImageFieldとして定義する
    icon = models.ImageField(upload_to="image/", blank=True, null=True)
    TYPE_CHOICES = (('company', '企業アカウント'),
                    ('general', '一般アカウント'))

    acctype = models.CharField(choices=TYPE_CHOICES, max_length=100, default='general')
    user_post=models.ForeignKey('posts.Post', on_delete=models.CASCADE,related_name='students',blank=True, null=True)
    # 作成を成功したら'ginstagram:profile'と定義されているURLに飛ぶ
    def get_absolute_url(self):
        return reverse(
            'ginstagram:profile', kwargs={'username': self.username})


class Connection(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User ,on_delete=models.CASCADE,related_name='following')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} : {}".format(
            self.follower.username,
            self.following.username)