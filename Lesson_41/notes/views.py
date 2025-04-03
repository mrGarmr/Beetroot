from django.shortcuts import get_object_or_404, redirect, render

from note_app.forms import NoteForm

from .models import Note, Category

# Create your views here.

def index(request):

    notes = Note.objects.all()


    return render(request, "notes/index.html", {"notes": notes})

def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, "notes/create_note.html", {"form": form})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        note.delete()
        return redirect('index')
    return render(request, "notes/delete_note.html", {"note": note})


def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm(instance=note)
    return render(request, "notes/edit_note.html", {"form": form, "note": note})


def note_info(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, "notes/note_info.html", {'title': note.title,
                                                    'text': note.text, 
                                                    'reminder': note.reminder, 
                                                    'category': note.category,
                                                    })




   