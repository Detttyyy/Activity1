from django.urls import path
from .views import HomePageView, AboutPageView, NavbarPageView, ContactPageView, ServicesPageView, ProductPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('navbar/', NavbarPageView.as_view(), name='navbar'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('product/', ProductPageView.as_view(), name='product')
]