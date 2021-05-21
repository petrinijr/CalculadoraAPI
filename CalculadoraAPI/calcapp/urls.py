from django.urls import path
from . import views

urlpatterns = [
    path('tests', views.ViewTests.as_view()),
    path('corinthians', views.corinthians),
]