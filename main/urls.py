from    django.urls import path

from main.apps import MainConfig
from main.views import home, contacts, product

app_name = MainConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>product/', product, name='product'),
]

