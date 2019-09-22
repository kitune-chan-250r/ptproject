from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from .forms import CustomUserCreationForm, PostForm
from .models import Post, User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import ModelFormMixin

class SignUpView(CreateView):
    form_class = CustomUserCreationForm #UserCreationForm
    success_url = reverse_lazy('complete') #登録成功時にリダイレクトする先
    template_name = 'create.html'

class SignUpCompView(TemplateView):
    template_name = 'registration/login.html'

#[develop branch]-added
class IndexView(TemplateView):
    template_name = 'index.html'
    form_class = PostForm

#[develop branch]-added
#投稿と表示機能
@login_required
def post_create(request):
    if request.method == 'POST':
        author = Post(author=User.objects.get(pk=request.user.id))
        #author = User.objects.get(pk=request.user.id)
        form = PostForm(request.POST or None, instance=author)
        form.save(commit=False)
        if form.is_valid():
            form.save()
            posts = Post.objects.all()
            return render(request, 'index.html', {'form':form, 'posts': posts})
        else:
            return HttpResponse('無効な値です')
    else:
        form = PostForm()
        posts = Post.objects.all()
    return render(request, 'index.html', {'form':form, 'posts': posts})

#投稿の表示を別ページにする場合に渡すlistview
'''
@login_required
def listView(request):
    posts = Post.object.all()
    return render(request, index.html, {'posts': posts})

'''