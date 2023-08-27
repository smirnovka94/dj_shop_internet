from    django.urls import path

from main.views import index, result

urlpatterns = [
    path('', index),
    path('', result)
]

