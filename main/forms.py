# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from .models import Person

# Create your models here.
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name','age','address']
        