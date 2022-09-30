from rest_framework import serializers
from notes.models import *
from django.contrib.auth import get_user_model


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
    author = serializers.SerializerMethodField(read_only=True) #для закрытия редактирования автора заметки
    def get_author(self, obj): #для определения выводимого атрибута связанного поля (по умолчанию - id)
        return str(obj.author.email)

    class Meta:
        model = Note
        fields = '__all__'
class ThinNoteSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='notes-detail')

    class Meta:
        model = Note
        fields = ('id', 'title', 'url')



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        queryset = model.objects.all()
        fields = ('id', 'email', 'password', 'name', 'is_admin')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = self.Meta.model(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password', ''))
        return super.update(instance, validated_data)