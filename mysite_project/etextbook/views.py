import os
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import UploadFileForm

from utilities.etextbookSearch import parse_bookstore_csv


class SpreadsheetView(FormView):
    form_class = UploadFileForm
    template_name = 'etextbook/spreadsheet_page.html'
    success_url = reverse_lazy('etextbook:upload')

    def form_valid(self, form):
        convert_csv(self.request)
        form.save()
        return super().form_valid(form)


def convert_csv(request):
    filename = request.FILES['document'].name
    orig_csv = os.path.join('uploaded_spreadsheets', filename)
    new_csv = os.path.join('uploaded_spreadsheets', "cleaned_{}".format(filename))
    parse_bookstore_csv.main(orig_csv, new_csv)
    return_spreadsheet(request, filepath=new_csv)


def return_spreadsheet(request, filepath=None):
    filename = os.path.split(filepath)[-1]
    with open(filepath, 'r', encoding='utf-8') as f:
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
        return response
