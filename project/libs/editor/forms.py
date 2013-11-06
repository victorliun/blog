from django import forms

from models import Article

class ArticleForm(forms.ModelForm):
    """ Form for article"""

    class Meta:
        model = Article
        fields = ["title", "category"]

