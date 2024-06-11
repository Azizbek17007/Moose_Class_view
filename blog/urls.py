from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('article', ArticlePageView.as_view(), name='article'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
]