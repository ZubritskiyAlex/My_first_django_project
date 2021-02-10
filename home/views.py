from django.views.generic import DetailView, ListView
from home.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    ordering = "title"
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article.html"
    pk_url_kwarg = "pk"
    context_object_name = "obj"



