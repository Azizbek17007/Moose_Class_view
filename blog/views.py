from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from pip._vendor.rich.markup import Tag

from .form import CommentForm

from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView

from blog.models import *

class HomePageView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    queryset = Article.objects.all().order_by('id')

class ArticlePageView(ListView):
    model = Article
    template_name = 'blog.html'
    context_object_name = 'articles'
    paginate_by = 3

    def get_queryset(self):
        return Article.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_list = Article.objects.all().order_by('id')
        paginator = Paginator(article_list, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            article_list = paginator.page(page)
        except PageNotAnInteger:
            article_list = paginator.page(1)
        except EmptyPage:
            article_list = paginator.page(paginator.num_pages)

        context['article_list'] = article_list
        context['tags'] = Tag.objects.all()
        return context



class ArticleDetailView(DetailView, CreateView):
    model = Article
    template_name = 'blog-single.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article_id=self.kwargs['pk']).order_by('id')[:3]
        context['tags'] = self.request.GET.get('tags')
        return context

    def form_valid(self, form):
        post=self.get_object()
        comment=form.save(commit=False)
        comment.article= post
        comment.save()
        return redirect(f"/detail/{post.id}")


class AboutPageView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about'





