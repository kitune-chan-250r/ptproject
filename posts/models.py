from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE)
    picture = models.ImageField(
        upload_to="image/posts/", blank=True, null=True)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class Like(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)


# 以下追加
class Comment(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    text = models.TextField(blank=True)


