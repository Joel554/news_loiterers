from django.urls import path
from .views import ArticleDetailView, ArticleListView

app_name = "news"

urlpatterns = [
    path('', ArticleListView.as_view(), name="article-list"),
    path('<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
]