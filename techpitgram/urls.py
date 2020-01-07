from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('posts.urls')),  # postsのurls.pyへのパスを追加
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
