from django.shortcuts import render
from .models import Note

# Create your views here.

def index(request):
    notes = Note.objects.all()
    test_notes = [
        {"title": "First note", "content": "This is blah blah of First note."},
        {"title": "Second note", "content": "This is blah blah of Second note."},
        {"title": "Third note", "content": "This is blah blah of Third note."},
    ]
    return render(request, "notes/index.html", {"notes": test_notes})
