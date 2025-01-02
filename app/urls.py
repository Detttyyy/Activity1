from django.urls import path
from .views import (HomePageView, AboutPageView, NavbarPageView, ContactPageView, ServicesPageView, ProductPageView, 
BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('navbar/', NavbarPageView.as_view(), name='navbar'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('product/', ProductPageView.as_view(), name='product'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete')
]