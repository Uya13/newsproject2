from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsList.as_view(), name ='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    # path('create/', create_post, name='post_create')
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/update/', PostUpdate.as_view(), name = 'post_update'), 
    path('news/<int:pk>/delete/', PostDelete.as_view(), name = 'post_delete'), 
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/update/', ArticleUpdate.as_view(), name = 'article_update'), 
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name = 'article_delete'), 
]