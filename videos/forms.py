from django import forms
from .models import Video

from django import forms


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'file']


from django import forms

class SubtitleSearchForm(forms.Form):
    query = forms.CharField(label='Search Query', max_length=100)
