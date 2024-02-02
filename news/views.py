from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from typing import Any

from .models import Article


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'news/article_list.html', {'articles': articles})


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'news/article_detail.html', {'article': article})

class ArticleListView(generic.ListView):
    model = Article
    # paginate_by = 1
    context_object_name = "articles"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    
    def get_queryset(self):
        user = self.request.user
        queryset = Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]
        return queryset


class ArticleDetailView(generic.DetailView):
    model = Article
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        
        return context

