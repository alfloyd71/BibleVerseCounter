from django.urls import path
from chaptersverses.views import getNumberOfChaptersVerses



urlpatterns = [
    path('', getNumberOfChaptersVerses, name='getNumberOfChaptersVerses')
]