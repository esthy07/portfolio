from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from Me.models import CategorieProjet
from .models import *

# Create your views here.
def blog(request):
    context = {
        'state':0
    }
    return render(request, 'blog.html', context)

def blog_detail(request):
    return render(request, 'blog-single.html')


class ArticleDetail(DetailView):
    model = Article
    template_name='blog-single.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context['categories'] = CategorieArticle.objects.all()
        context['state'] = 1
        context['articles'] = Article.objects.filter(status=True).order_by("-created")[:3]
        return context


class ArticleListView(ListView):
    model = Article
    paginate_by = 100
    context_object_name = "articles"
    template_name = "blog.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['state'] = 0 
        return context
        