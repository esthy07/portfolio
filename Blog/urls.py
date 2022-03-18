
from . import views
from django.urls import path


urlpatterns = [
    path('home', views.ArticleListView.as_view(), name='blog'),
    path('blog-detail/<int:pk>', views.ArticleDetail.as_view(), name='blog-detail')
]