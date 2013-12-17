# Create your views here.
from django.shortcuts import render_to_response
from news.models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)

    return render_to_response('news/year_archive.html', {'year': year, 'article_list': a_list})

def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)

    return render_to_response('news/year_archive.html', {'year': year, 'month':month, 'article_list': a_list})
