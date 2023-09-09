from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from notes.models import Note


def index(request: HttpRequest) -> HttpResponse:
    notes = Note.objects.all()
    
    return render(request, 'notes/index.html', {
        'notes': notes,
    })
