import datetime

from django.views.generic import TemplateView


class FrontView(TemplateView):
    template_name = 'site_core/frontpage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        description_text = ["""This page is an example of a basic template.  Other pages inherit from this template.""",
        """For example, this text is in a block that is overridden by blocks in other pages.  Other blocks are designed to not be overridden (i.e., the header, sidebar, etc.).""",
        """Google Domains manages the domain name, linking the Type A resource records to the Amazon EC2 elastic IP address.  It also forwards emails sent to this website.""",
        """Let's Encrypt provides the https certification.""",
        """Amazon EC2 hosts the ubuntu server.  AWS limits access for ssh, etc. to my IP address.  Within that server, Uncomplicated Firewall (ufw) further limits permitted network traffic.""",
        """Nginx serves the static content and passes other requests to gunicorn.  Django takes requests from and gives responses to gunicorn, and is connected to a mysql database.  Because the box is small and has little traffic, there is no cost except the annual domain name registration.""",
        "Within the django server, two settings files are available:  production and development.  This allows anyone to <code>git clone https://github.com/GarrettArm/TheDjangoBook</code> then run the server on their computer <code>python manage.py runserver --settings=site_core.settings.development </code>",
        ]
        context['description'] = description_text
        return context

class CurrentDateView(TemplateView):
    template_name = 'dateapp/current_datetime.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        context['current_datestuff'] = current_time
        description_text = ["This simple page shows how to insert a bit of information into the response.  A function asks for the current time and formats it as human-readable text.  That text gets added to the context.  The template then asks for that context information and displays it within the response html.", ]
        context['description'] = description_text
        return context
