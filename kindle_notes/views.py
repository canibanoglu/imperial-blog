from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from kindle_notes.models import Note, Book
from kindle_notes.clippings_parser import *

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
    notes = Note.objects.filter(book__pk = pk).order_by('-date')
    book = Book.objects.get(pk=pk)
    stuff = {'notes': notes, 'book': book}
    return render_to_response('kindle_notes/notes.html', stuff, context)
