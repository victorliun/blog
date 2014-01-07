"""
This views.py managers how to create/modify/delete diary
"""
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse

from apps.diary.models import Diary
from apps.diary.forms import DiaryForm

class CreateDiaryView(CreateView):
    "displays editing article page"
    
    model = Diary
    form_class = DiaryForm
    template_name = "diary/diary_new.html"
 
    def post(self, request, *args, **kwargs):
    	title = request.POST.get('title')
    	category = request.POST.get('category')
    	text = request.POST.get('diary_main')

    	diary = self.model.objects.create(title=title, category=category)
        file_path = diary.writeToXML(text)
        if file_path:
            diary.xml_path = file_path
            diary.save()
            return HttpResponse("Diary saved.")
        else:
            diary.delete()
            return HttpResponse("Failed to save diary.")
   	def get(self, request, *args, **kwargs):
   		
   		return super(CreateDiaryView, self).get(request, *args, **kwargs)


class UpdateDiaryView(UpdateView):
    """ view for updating diary"""

    model = Diary
    template_name = "diary/diary_new.html"

    def get_context_data(self, **kwargs):

        context = super(UpdateDiaryView, self).get_context_data(**kwargs)
        context['action'] = reverse('diary-edit',
                                    kwargs={'pk': self.get_object().id})
        return context


class DeleteDiaryView(DeleteView):
    """View for delete a diary"""

    model = Diary

class ListDiaryView(ListView):
    """ view for updating diary"""

    model = Diary
    template_name = "diary/diary_list.html"

    def get(self, request, category):
        print category
        return super(ListDiaryView, self).get(request, *args, **kwargs)

class DetailDiaryView(DetailView):
    """ view for updating diary"""

    model = Diary
    template_name = "diary/diary_detail.html"

    def get_context_data(self, **kwargs):
        """Populate all context of the template with all setting configures"""
        
        context = super(DetailDiaryView, self).get_context_data(**kwargs)
        context['action'] = reverse('diary-detail',
                                    kwargs={'pk': self.get_object().id})

        return context
