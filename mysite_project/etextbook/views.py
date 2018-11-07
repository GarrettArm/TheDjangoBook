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

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response = convert_csv(self.request)
            return response
        else:
            return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        description = ["""This page was a successful experiment.  I had been responsible for running a script for a coworker each semester, and could not install python on her computer so that she could run the script herself.  To streamline the process, and make the functionality accessible, I folded the script into a webapp.""",
        """You became familiar with models and forms from the Contact Us page.  This page extends that knowledge, to running scripts not included in the django framework.  We <a href=https://github.com/GarrettArm/TheDjangoBook/blob/master/mysite_project/etextbook/views.py>dropped down a level of abstraction</a> and replaced the default FormView reaction to Post requests.""",
        """Following a valid Post request, the form is saved to database and a custom function "convert_csv()" is run - with the output file returned to the user as an http response.""",
             ]
        context['description'] = description
        return context


def convert_csv(request):
    request_file = request.FILES['document']
    uploaded_file = request_file.open().readlines()
    cleaned_csv_list = parse_bookstore_csv.cleanup_original_text(uploaded_file)
    response = HttpResponse(content_type='text/csv')
    cleaned_filename = 'cleaned-{}'.format(request_file.name)
    response['Content-Disposition'] = 'attachment; filename={}'.format(cleaned_filename)
    writer = csv.writer(response,
                        delimiter='\t',
                        quotechar='"',
                        quoting=csv.QUOTE_ALL)
    for line in cleaned_csv_list:
        writer.writerow(line)
    return response
