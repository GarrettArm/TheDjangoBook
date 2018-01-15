import os

from django import forms
from .models import Document


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

    def clean_document(self):
        data = self.cleaned_data['document']
        filename = data.name
        if os.path.splitext(filename)[1] != '.csv':
            raise forms.ValidationError('The file must be a csv.')
        return data
