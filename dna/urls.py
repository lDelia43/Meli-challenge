from django.urls import path
from .views import mutant_view

urlpatterns = [
    path('mutant/', mutant_view, name='mutant'),
]
