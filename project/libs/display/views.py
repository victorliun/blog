# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.conf import settings
from libs.editor.models import Article
from libs.editor.forms import ArticleForm

class DisplayView(TemplateView):
    "displays single article"
    
    template_name = "display/travel.html"
    
    def get_context_data(self, **kwargs):
        """Populate all context of the template with all setting configures"""
        
        context = super(DisplayView, self).get_context_data(**kwargs)
#        context.update({'STATIC_URL':settings.STATIC_URL})
   
        context['id'] = kwargs['article_id']

        article = Article.objects.get(pk=context['id'])
        context['article'] = article
        context['section'] = article.parseXML()
        context['form'] = ArticleForm()

        return context

   

    
