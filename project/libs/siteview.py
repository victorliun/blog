# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.conf import settings

class SiteView(TemplateView):
    """
    SiteView is the parent view for this site, every coming up view should inherit this view
    to get basic configures.
    """
    
    template_name = "base/base.html"
    
    def get_context_data(self, **kwargs):
        """Populate all context of the template with all setting configures"""
        
        context = super(HomepageView, self).get_context_data(**kwargs)
        context.update({'STATIC_URLL':settings.STATIC_URL})
        
        return RequestContext(context)

    
