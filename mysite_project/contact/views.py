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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        description = ["This page uses Forms, which allow user input.",
        "Each field is validated.  For example, an invalid email addresses will spawn an error message.  The criteria for validation come directly from the database Model we created, although you can override or augment those criteria if you wish.",
        "If all the fields are valid, django will then carry out whatever steps you named.  For example, we save the fields to a database and send an email to the administrator.", ]
        context['description'] = description
        return context        


class ThanksView(TemplateView):
    template_name = 'contact/thanks_page.html'
