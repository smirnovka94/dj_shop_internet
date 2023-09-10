from django.urls import path

from main.apps import MainConfig
from main.views import home, contacts, ProductListView, ProductDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
]

