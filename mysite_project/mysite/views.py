from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail, get_connection

import datetime
import os

from mysite.forms import ContactForm


def hello(request):
    return HttpResponse('Hello world')


def current_date(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    context = {'current_datestuff': current_time}
    template_path = os.path.join('dateapp', 'current_datetime.html')
    return render(request, template_path, context)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    incremented_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    context = {'hour_offset': offset, 'incremented_time': incremented_time, }
    template_path = os.path.join('dateapp', 'future_datetime.html')
    return render(request, template_path, context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con,
            )
            return HttpResponseRedirect('/contact/thanks')
    else:
        form = ContactForm(initial={'subject': 'initial text, weird'})
    return render(request, 'contact_form.html', {'form': form, })


def thanks_logic(request):
    return render(request, 'thanks_page.html', )


def review_details(request, year, month, day):
    sum = int(year) + int(month) + int(day)
    text = "Year: {}, Month: {}, Day {}, which add to {}".format(year, month, day, sum)
    return HttpResponse(text)
