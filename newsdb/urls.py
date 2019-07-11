from django.urls import path

from . import views

app_name = 'newsdb'
urlpatterns = [
    path('', views.NewsList.as_view(), name='news_list'),
    path('<int:pk>/', views.NewsDetail.as_view(), name='news_detail'),
    path('tag/<str:tag_name>/', views.NewsByTag.as_view(), name='news_by_tag'),
]
