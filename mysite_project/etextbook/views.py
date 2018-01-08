import os
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from utilities.etextbookSearch import parse_bookstore_csv


def read_spreadsheet(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filename = request.FILES['document'].name
            if os.path.split(filename)[1] != '.csv':
                form = UploadFileForm()
                return render(request, 'etextbook/spreadsheet_page.html', {'form': form, 'errors': ['Uploaded file must be a csv.']})
            orig_csv = os.path.join('uploaded_spreadsheets', filename)
            new_csv = os.path.join('uploaded_spreadsheets', "cleaned_{}".format(filename))
            parse_bookstore_csv.main(orig_csv, new_csv)
            form.save()
            return return_spreadsheet(request, filepath=new_csv)
    else:
        form = UploadFileForm()
    return render(request, 'etextbook/spreadsheet_page.html', {'form': form})


def return_spreadsheet(request, filepath=None):
    filename = os.path.split(filepath)[-1]
    with open(filepath, 'r', encoding='utf-8') as f:
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        return response
