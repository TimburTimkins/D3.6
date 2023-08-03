from django.urls import path
from .views import NewsList, NewsDetail, multiply, create_news


urlpatterns = [
   path('', NewsList.as_view()),
   path('<int:pk>', NewsDetail.as_view()),
   path('multiply/', multiply),
   path('create/', create_news, name='news_create'),
]