from django.shortcuts import render
from rest_framework.decorators import api_view
from notes.models import Note
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


#через вьюсеты
class NotesView(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    #для переопределения сериалайзера для усечения отображения полей. Если не нужно переопредделять, то эта функция не нужна
    def list(self, request, *args, **kwargs):
        notes = Note.objects.all()
        context = {'request': request}
        serializer = ThinNoteSerializer(notes, many=True, context=context)
        return Response(serializer.data)


#через дженерики
# class NotesList(ListCreateAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#
#     def list(self, request, *args, **kwargs):
#         notes = Note.objects.all()
#         context = {'request': request}
#         serializer = ThinNoteSerializer
#         return Response (serializer.data)
#
#
# class NotesDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#
#
#
# определяем через миксин
#
# class NotesList(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#
#     def get(self, request, *args, **kwargs):
#         self.serializer_class = ThinNoteSerializer
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


#определяем через функцию
# @api_view(['GET', 'POST']) # функция отображения записей и создания записи
# def notes_list(request, fotmat=None):
#     if request.method == 'GET':
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #определяем через класс
# class NotesList(APIView):
#     def get(self, request, formate=None):
#         notes = Note.objects.all()
#         context = {'request': request}
#         serializer = ThinNoteSerializer(notes, many=True, context=context)
#         return Response(serializer.data)
#
#     def post(self, request, formate=None):
#         serializer = NoteSerializer(data=request.data)


#определяем через функцию
# @api_view(['GET', 'PUT', 'DELETE'])
# def notes_detail(request, pk, fotmat=None):
#     try:
#         note = Note.objects.get(pk=pk)
#     except Note.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = NoteSerializer(note, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)status
#
# #определяем через класс
# class NotesDetailView(APIView):
#     def get_object(self, pk, format=None):
#         try:
#             note = Note.objects.get(pk=pk)
#             return note
#         except Note.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#     def get(self, request, pk, format=None):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         note = self.get_object(pk)
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
