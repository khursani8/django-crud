# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Person
from .forms import PersonForm
# Create your views here.
def index(request):
    p = Person.objects.all()
    form = PersonForm()
    return render(request,'index.html',{'person':p,'form':form})

def post_person(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
    return redirect('index')
    
def update_person(request,id):
    if id:
        person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None,instance=person)
    return render(request,'update.html',{'person':person,'form':form})

def update(request,id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST,instance=person)
    if form.is_valid():
        form.save(commit=True)
    return redirect('index')

def delete(request,id):
    person = get_object_or_404(Person, pk=id).delete()
    return redirect('index')
