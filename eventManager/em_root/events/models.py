from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

CATEGORIES = (
    ('CONFERENCIA', 'Conferencia'),
    ('SEMINARIO', 'Seminario'),
    ('CONGRESO', 'Congreso'),
    ('CURSO', 'Curso'),
)


PRESENCIAL_VIRTUAL = (
    ('PRESENCIAL', 'Presencial'),
    ('VIRTUAL', 'Virtual')
)


class Event(models.Model):
    IdEvent = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    startDate = models.DateTimeField()
    finishDate = models.DateTimeField()
    presencial = models.CharField(max_length=50, choices=PRESENCIAL_VIRTUAL)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class AddEventForm(ModelForm):
    
    class Meta:
        model = Event
        fields = ['name', 'category', 'location', 'address', 'startDate', 'finishDate', 'presencial']
