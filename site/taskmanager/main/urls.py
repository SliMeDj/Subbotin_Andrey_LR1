from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('nineCLASS', views.nineCLASS, name='9cl'),
    path('elevenCLASS', views.elevenCLASS, name='11cl'),
    path('contact', views.contact, name='cont'),
    path('create', views.create, name='create'),
    path('VPR', views.vpr, name='vpr')
]
