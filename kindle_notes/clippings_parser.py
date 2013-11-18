from datetime import datetime
from kindle_notes.models import Book, Note


def kindle_clippings_parser(fin):
    """
    This helper function expects a file descriptor fin as an argument
    and will create Book and Note objects using the contents of the 
    file descriptor object.
    """

    data = fin.read().split("==========")

    objects = [d.strip().split("\r\n") for d in data if 'Bookmark' not in d]

    # Discard the last element because it is useless
    objects.pop(-1)

    books = dict()
    notes = dict()

    for obj in objects:
        book, note, note_body = kindle_extract_info(obj)
        books.setdefault(book['title'],
                Book.objects.get_or_create(title=book['title'],
                                           author=book['author'])[0])
        notes.setdefault(note['datetime'], note)[note_body['type']] = note_body['body']
        notes[note['datetime']]['book'] = books[book['title']]

    for note in notes.values():
        new_note = Note(date = note.get('datetime'),
                        highlight = note.get('highlight', ""),
                        note = note.get("note", ""),
                        page = note.get('page', ''),
                        location = note.get('location', ''),
                        book = note['book'])
        new_note.save()

def kindle_extract_info(l):
    title_info, page_info, dummy, body = l
    title, author = kindle_parse_title_info(title_info)
    note_type, page, location, dtime = kindle_parse_page_info(page_info)
    body = body.decode('utf-8')
    book_dict = {'title': title, 'author': author}
    note_dict = {'page': page, 'location': location,
                 'datetime': dtime.strftime('%Y-%m-%d %H:%M:%S')}
    type_dict = {'type': note_type.lower(), 'body': body}

    return (book_dict, note_dict, type_dict)

def kindle_parse_title_info(title_info):
    title, author = title_info.rsplit('(', 1)
    if title.startswith('\xef\xbb\xbf'):
        title = title[3:]
    title = title.strip()
    if ',' in author:
        author_lname, author_fname = author[:-1].split(', ')
        author = ' '.join((author_fname, author_lname))
    else:
        author = author[:-1]

    return (title, author)

def kindle_parse_page_info(page_info):
    page, location, dtime = page_info.split(' | ')
    dummy1, dummy2, note_type, dummy3, dummy4, page = page.split()
    location = location.rsplit(' ', 1)[-1]
    dtime = datetime.strptime(dtime.split(', ', 1)[1], '%B %d, %Y %I:%M:%S %p')
    return (note_type.lower(), page, location, dtime)

