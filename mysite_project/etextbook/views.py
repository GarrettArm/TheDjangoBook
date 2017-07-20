from django.shortcuts import render
from .forms import FileUploadForm

import os


def save_file(file):
    with os.open('/home/james/Desktop/filename.txt', 'wb+') as f:
        for chunk in file.chunks():
            print('writing')
            f.write(chunk)


def bookstore_spreadsheet(request):
    if request.method == 'POST':
        print('got post')
        form = FileUploadForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print('is_valid')
            save_file(request.FILES['file'])
            return render(request, 'etextbook/spreadsheet_page.html')
    else:
        form = FileUploadForm()
    return render(request, 'etextbook/spreadsheet_page.html', {'form': form} )
