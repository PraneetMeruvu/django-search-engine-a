from django import forms
from .models import MultipleFileUpload

class MultipleFileUploadForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = MultipleFileUpload
        fields = ('files',)