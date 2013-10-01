# Create your views here.
from django.http import HttpResponse

def homepage_view(request):
    "view for homepage"
    
    return HttpResponse("Welcome to my homepage")
