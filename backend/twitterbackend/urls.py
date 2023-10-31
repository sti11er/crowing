from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('message/create/', MessageCreateView.as_view()),
    path('registration/', RegistrationUser.as_view()),
    path('authentication/', AuthenticationUser.as_view()),
    path('message/all/', MessageListView.as_view())
]
