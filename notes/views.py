from django.http import (
    HttpRequest, HttpResponse,
    HttpResponseBadRequest, HttpResponseNotFound,
)
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from notes.models import Note


def index(request: HttpRequest) -> HttpResponse:
    notes = Note.objects.all()
    
    return render(request, 'notes/index.html', {
        'notes': [
            {
                'id': note.id,
                'content': note.content,
            }
            for note in notes
        ],
    })


@csrf_exempt
def update_note(request: HttpRequest) -> HttpResponse:
    try:
        body = json.loads(request.body)
    except ValueError:
        return HttpResponseBadRequest()
    
    try:
        note_id = body['id']
        content = body['content']
    except KeyError:
        return HttpResponseBadRequest()
    
    if not isinstance(note_id, int):
        return HttpResponseBadRequest()
    
    if not isinstance(content, str):
        return HttpResponseBadRequest()
    
    try:
        note = Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return HttpResponseNotFound()
    
    note.content = content
    note.save(update_fields=['content'])
    
    return HttpResponse()
