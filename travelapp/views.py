from django.shortcuts import render
from django.views.generic import TemplateView

# Define the class-based view
class FrontpageView(TemplateView):
    # Specify the template name
    template_name = 'index.html'

class ContactpageView(TemplateView):
    # Specify the template name
    template_name = 'contact.html'

class UdupiPage(TemplateView):
    template_name = 'udupi.html'

class mookambikaPage(TemplateView):
    template_name = 'mookambika.html'

class murudeswarPage(TemplateView):
    template_name = 'murudeswar.html'


class shringeriPage(TemplateView):
    template_name = 'shringeri.html'

class aboutPage(TemplateView):
    template_name = 'about.html'