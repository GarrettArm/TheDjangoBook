import datetime

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class FrontView(TemplateView):
    template_name = 'site_core/frontpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        description_text = ["""This page is an example of a basic <a href=https://en.wikipedia.org/wiki/Web_template_system>template</a>.  Templating lets you break the view up into things that change from page to page, and things that remain the same across the site.  The sidebar, for example, never changes -- so it's hardcoded in the <a href=https://github.com/GarrettArm/TheDjangoBook/blob/master/mysite_project/templates/base.html>base template html</a>.  But the title text, main block, etc. do change, and they are wrapped in blocks.""",
        """Google Domains manages the domain name, linking the gaularmstrong.com resource records to the Amazon EC2 elastic IP address.""",
        """Amazon EC2 hosts the ubuntu server.  AWS allows ssh, etc. from only my IP address; it allows https from everyone else.  Within that server, Uncomplicated Firewall (ufw) further limits permitted network traffic.""",
        """Let's Encrypt provides the https certification.""",
        """Nginx serves the static content (i.e., images, css, etc) and passes other requests to gunicorn.  Gunicorn runs several copies of the Django appserver, like mod_php for apache.  Django takes requests from gunicorn, processes them, and gives responses back to gunicorn.  Django is connected to a sql database.""",
        """Because the box is small and has little traffic, there is no cost except the annual domain name registration.""",
        ]
        context['description'] = description_text
        return context


class CurrentDateView(TemplateView):
    template_name = 'dateapp/current_datetime.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        context['current_datestuff'] = current_time
        description_text = ["""This simple page shows how to insert a bit of information into the response.""",
        """When the Django app gets the request for this page, it runs <a href=https://github.com/GarrettArm/TheDjangoBook/blob/master/mysite_project/site_core/views.py>a little extra function "get context data"</a>:  it looks up the current time and it adds that information into the context.""",
        """When the <a href=https://github.com/GarrettArm/TheDjangoBook/blob/master/mysite_project/templates/dateapp/current_datetime.html>template</a> gets handed the context and told to make some html, it puts the square peg into the square hole, etc, then sends the generated html to gunicorn as response html.""", ]
        context['description'] = description_text
        return context


class MyLogoutView(LogoutView):
    next_page = '/'


class MyLoginView(LoginView):
    pass


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'site_core/signup.html'


# def register(request):
#     if request.method == 'POST':
#         f = UserCreationForm(request.POST)
#         if f.is_valid():
#             f.save()
#             message.success(request, 'Account created successfully')
#             return redirect('signup')
#     else:
#         f = UserCreationForm()
#     return render(request, 'site_core/register.html', {'form': f})


