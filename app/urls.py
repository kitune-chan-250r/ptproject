from django.urls import path, include
from .views import SignUpView,  post_create, user_detail, user_prof_update
from django.views.generic import TemplateView

urlpatterns = [
    path('new/', SignUpView.as_view()),
    #path('complete/', SignUpCompView.as_view(), name='complete'),
    #[develop branch]-added
    path('index/', post_create, name='index'),#TimeLineAndPostView or post_create
    path('detail/', user_detail, name='detail'),#ユーザーページ
    path('profupdt/', user_prof_update, name='profupdt')#プロフ更新ページ
]