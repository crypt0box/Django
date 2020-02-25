from django.views import generic
from django.contrib.auth.views import LoginView
from .models import Post
from .forms import LoginForm


class IndexView(generic.ListView):
    model = Post


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'ThreeLineDiary/login.html'
