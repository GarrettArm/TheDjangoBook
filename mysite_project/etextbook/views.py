import csv

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import UploadFileForm

from utilities.etextbookSearch import parse_bookstore_csv


class SpreadsheetView(FormView):
    form_class = UploadFileForm
    template_name = 'etextbook/spreadsheet_page.html'
    success_url = reverse_lazy('etextbook:upload')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response = convert_csv(self.request)
            return response
        else:
            return render(request, self.template_name, {'form': form})


def convert_csv(request):
    request_file = request.FILES['document']
    uploaded_file = request_file.open().readlines()
    cleaned_csv_list = parse_bookstore_csv.cleanup_original_text(uploaded_file)
    response = HttpResponse(content_type='text/csv')
    cleaned_filename = 'cleaned-{}'.format(request_file.name)
    response['Content-Disposition'] = 'attachment; filename={}'.format(cleaned_filename)
    writer = csv.writer(response,
                        delimiter=',',
                        quotechar='"',
                        quoting=csv.QUOTE_ALL)
    for line in cleaned_csv_list:
        writer.writerow(line)
    return response
