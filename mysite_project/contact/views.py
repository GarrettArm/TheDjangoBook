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
        description = ["""This page uses Forms, which allow user input.""",
            """When defining each data Model, you specify what fields the model has.    The particular <a href=https://github.com/GarrettArm/TheDjangoBook/blob/master/mysite_project/contact/models.py>model</a> created for this page has fields: subject, email, message, and time created.  You also specify the qualities of each attribute.  For example, the email attribute is an EmailField.  Django translates the abstract Model into an actual SQL table with appropriate columns and datatypes.""",
            """Forms can inherit from one or more data Models.  The code for this <a href=https://github.com/GarrettArm/TheDjangoBook/blob/master/mysite_project/contact/forms.py>form</a> can be verbalized as, "Use the Comment model and only include fields: subject, email, and message.  The rest of the logic is provided by the django framework.""",
            """Validation is built into the framework.  For example, our Email field expects a normal email address, and will spawn an error message otherwise.  The criteria for validation come directly from the Model we defined, although you can override or augment those criteria if you wish.  The Message field has an added validator to ensure that the submitted message is more than 4 words long.""",
            """If all the fields are valid, django will accept the submission and carry out whatever <a href=https://github.com/GarrettArm/TheDjangoBook/blob/master/mysite_project/contact/views.py>steps you defined</a>.  For example, here we save the fields to a database, send an email to the administrator, and redirect to a "success" page""",
             ]
        context['description'] = description
        return context        


class ThanksView(TemplateView):
    template_name = 'contact/thanks_page.html'
