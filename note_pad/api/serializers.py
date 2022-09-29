from rest_framework import serializers
from notes.models import *

# class NoteSerializer(serializers.Serializer): #способ 1
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True)
#     text = serializers.CharField(required=False, allow_blank=True)
#
#     def create(self, validated_data):
#         return Note.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.text = validated_data.get('text', instance.text)
#         instance.save()
#         return instance

class NoteSerializer(serializers.ModelSerializer):


    class Meta:
        model = Note
        fields = '__all__'
class ThinNoteSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='notes-detail')

    class Meta:
        model = Note
        fields = ('id', 'title', 'url')
