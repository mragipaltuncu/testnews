from django.shortcuts import render
from django.views import generic
from .getnews import news
from .models import ArticleTitle
# Create your views here.

class HomeView(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self,**kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        context['news'] = ArticleTitle.objects.all()
        return context