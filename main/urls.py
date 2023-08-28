from    django.urls import path

from main.views import home, contacts

urlpatterns = [
    path('', home, name='home'),
    path('', contacts, name='contacts')
]

