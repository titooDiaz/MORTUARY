from django.urls import path

# views main
from main.views import homePage


urlpatterns = [
    path('', homePage.as_view(), name='homePage'),
]