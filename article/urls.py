from django.urls import include, path, re_path
from article import views


urlpatterns = [
    path('<str:a>', views.article, name='articles'),
]