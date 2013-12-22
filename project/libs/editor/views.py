"""
This views.py managers how to create/modify/delete article
"""
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.conf import settings
from libs.editor.models import Article
from libs.editor.forms import ArticleForm

class EditorView(TemplateView):
    "displays editing article page"
    
    template_name = "display/new_article.html"
    
    def get_context_data(self, **kwargs):
        """Populate all context of the template with all setting configures"""
        
        context = super(EditorView, self).get_context_data(**kwargs)
        
        if kwargs.has_key('article_id'):
            context['id'] = kwargs['article_id']
            article = Article.objects.get(pk=context['id'])
            context['article'] = article
            context['section'] = article.parseXML()
        else:
            context['form'] = ArticleForm()

        return context