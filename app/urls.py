from django.contrib import admin
from django.urls import path, include
from .views import SignUpView, SignUpCompView, post_create, user_detail, user_prof_update


urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', SignUpView.as_view()),
    path('complete/', SignUpCompView.as_view(), name='complete'),
    #[develop branch]-added
    path('index/', post_create, name='index'),#TimeLineAndPostView or post_create
    path('detail/', user_detail, name='detail'),#ユーザーページ
    path('profupdt/', user_prof_update, name='profupdt')#プロフ更新ページ
]