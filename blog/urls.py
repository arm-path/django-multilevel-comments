from django.urls import path
from .views import *

urlpatterns = [
    path('', PrimaryPageBlog.as_view(), name='blog_primary'),
    path('blog-page/<str:slug>/', PageBlog.as_view(), name='blog_page'),
    path('blog-page/likes_or_dislikes/<str:slug>', сhange_model_comment, name ='comment_likes_or_dislikes'),
   
]
