from django.shortcuts import render

from .models import Note, Category

# Create your views here.

def index(request):

    notes = Note.objects.all()


    return render(request, "notes/index.html", {"notes": notes})
