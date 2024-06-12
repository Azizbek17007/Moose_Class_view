from django.urls import path

from config import settings
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('articles', ArticlePageView.as_view(), name='articles'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
]

