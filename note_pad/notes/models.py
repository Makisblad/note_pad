from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, SET_NULL
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Note(Model):
    author = ForeignKey(User, on_delete=SET_NULL, null=True, blank=False)
    title = CharField(max_length=250, verbose_name='Заколовок')
    text = TextField(blank=True, verbose_name='Текст')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'


