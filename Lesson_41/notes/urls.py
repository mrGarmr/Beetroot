from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("note/create/", views.create_note, name="create_note"),
    path("note/<int:note_id>/", views.note_info, name="note_info"),
    path("note/edit/<int:note_id>/", views.edit_note, name="edit_note"),
    path("note/delete/<int:note_id>/", views.delete_note, name="delete_note"),
]