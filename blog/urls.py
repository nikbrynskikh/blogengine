from django.urls import path
from .views import *


urlpatterns = [
    path('', posts_list, name='posts_list_url'), #отображение списка постов
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url' ), #отображает отдельный пост
    path('tags/', tags_list, name='tags_list_url'), #отображение списка тегов
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'), #отображает отдельный тэг
]