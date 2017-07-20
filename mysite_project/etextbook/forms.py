from django import forms


class FileUploadForm(forms.Form):
    filebox = forms.FileField(label="Select the raw bookstore spreadsheet")
