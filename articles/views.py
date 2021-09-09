from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView

from articles.forms import CommentForm
from articles.models import Article, Comment


class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'
class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'
class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'
    def dispatch(self, request, *args, **kwargs):
        obj=self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)
class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title','picture','body',)
    login_url = 'login'

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)





class CommentCreateView(LoginRequiredMixin,CreateView):

    model = Comment
    template_name = 'comment_new.html'
    fields = ('comment',)
    login_url = 'login'
    queryset = Article.objects.all()
    context_object_name = queryset


    def deteil(self,request,pk):
        obj=Article.objects.get(id=pk)
        return render(request,self.template_name,{'obj':obj})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article=Article.objects.get(id=self.kwargs['pk'])
        obj=Article.objects.get(id=self.kwargs['pk'])

        return super().form_valid(form)

class combineView(LoginRequiredMixin,View):
    form_class = CommentForm
    initial = {'key': 'value'}
    template_name = 'comment_new.html'
    login_url = 'login'
    model_name=Comment


    def get(self,request,*args,**kwargs):
        form = self.form_class(initial=self.initial)
        obj=Article.objects.get(id=self.kwargs['pk'])
        return render(request, self.template_name, {'form':form,'obj':obj})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.author = self.request.user
        form.instance.article=Article.objects.get(id=self.kwargs['pk'])
        if form.is_valid():
            form.save(self)

            return HttpResponseRedirect('/articles/')

        return render(request, self.template_name, {'form': form})
