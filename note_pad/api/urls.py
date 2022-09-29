from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns #для отображения данных в формате JSON


urlpatterns = [
    path('notes/', NotesList.as_view()),
    path('notes/<int:pk>/', NotesDetailView.as_view(), name='notes-detail')

]

urlpatterns =format_suffix_patterns(urlpatterns)