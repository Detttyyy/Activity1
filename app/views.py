from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
        template_name = 'app/about.html'

class NavbarPageView(TemplateView):
    template_name = 'app/navbar.html'

class ContactPageView(TemplateView):
        template_name = 'app/contact.html'

class ServicesPageView(TemplateView):
    template_name = 'app/services.html'

class ProductPageView(TemplateView):
    template_name = 'app/product.html'

