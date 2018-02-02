from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from .forms import ContactForm


class ContactView(FormView):
    template_name = 'contact/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')

    def form_valid(self, form):
        form.send_email()
        form.save()
        return super().form_valid(form)


class ThanksView(TemplateView):
    template_name = 'contact/thanks_page.html'
