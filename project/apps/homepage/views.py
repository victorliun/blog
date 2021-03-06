# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

class HomepageView(TemplateView):
    "view for homepage"
    
    template_name = "homepages/sitehome.html"
    
    def get_context_data(self, **kwargs):
        """Populate all context of the template with all setting configures"""
        
        context = super(HomepageView, self).get_context_data(**kwargs)
        context.update({'STATIC_URL':settings.STATIC_URL})
        
        return context

    
