from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns #для отображения данных в формате JSON
from rest_framework.routers import DefaultRouter

#Для автоматического ветвления при использовании вьюсета

router =DefaultRouter()
router.register('notes', NotesView, basename='notes')
urlpatterns = router.urls

# urlpatterns = [
#     # path('notes/', NotesView.as_view({'get': 'list', 'post': 'create'}), name='notes-list'),
#     # path('notes/<int:pk>/', NotesView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='notes-detail'),
#
# ]

# urlpatterns =format_suffix_patterns(urlpatterns)