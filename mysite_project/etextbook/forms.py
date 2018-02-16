from django import forms

from .models import Document


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')

    def clean_document(self):
        data = self.cleaned_data['document']
        if data.content_type != 'text/csv':
            raise forms.ValidationError('The file must be a csv.')
        return data
