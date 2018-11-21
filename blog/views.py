from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

# Create your views here.
def posts_list(request):
    """Функция отображения списка постов"""
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts':posts})

class PostDetail(ObjectDetailMixin, View):
    """Класс, отображающий детали поста"""
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'


class TagDetail(ObjectDetailMixin, View):
    """Класс, отображающий детали о тэге"""
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'

class TagUpdate(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__exact=slug)


def tags_list(request):
    """Функция отображения списка постов"""
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})

