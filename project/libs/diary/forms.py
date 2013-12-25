from django import forms

from models import Diary

class DiaryForm(forms.ModelForm):
    """ Form for diary"""

    class Meta:
        model = Diary
        fields = ["title", "category"]

    def clean(self):
    	if not self.cleaned_data.get("title"):
            raise ValidateError("A diary must have a title")

        return self.cleaned_data

