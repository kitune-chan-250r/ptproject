from django.contrib import admin
from django.urls import path, include
from .views import SignUpView, SignUpComp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', SignUpView.as_view()),
    path('complete/', SignUpComp.as_view(), name='complete'),
]