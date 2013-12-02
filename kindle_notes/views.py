from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from kindle_notes.models import Note, Book
from kindle_notes.clippings_parser import *
from kindle_notes.forms import NoteForm

import datetime

def books_index(request):
    context = RequestContext(request)
    books = Book.objects.all()
    return render_to_response('kindle_notes/index.html', {'books': books}, context)

@login_required()
def books_upload(request):
    context = RequestContext(request)
    if request.method == 'POST':
        kindle_clippings_parser(request.FILES['file'])
        return HttpResponseRedirect('/sidious/')
    else:
        return render_to_response('kindle_notes/upload.html', {}, context)

def books_view_notes(request, pk):
    context = RequestContext(request)
    book = Book.objects.get(pk=pk)
    stuff = {'book': book}
    if request.method == 'POST':
        note_form = NoteForm(data=request.POST)

        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.book = book
            note.date = datetime.datetime.now()
            note.save()

    if request.user.is_authenticated():
        form = NoteForm()
        stuff['form'] = form
    notes = Note.objects.filter(book__pk = pk).order_by('-date')
    stuff['notes'] = notes
    return render_to_response('kindle_notes/notes.html', stuff, context)
