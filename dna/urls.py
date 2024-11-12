from django.urls import path
from .views import mutant_view, stats_view

urlpatterns = [
    path('mutant/', mutant_view, name='mutant'),
    path('stats/', stats_view, name='stats')
]
