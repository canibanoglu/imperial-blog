This is a tentative list of things that I plan to add to impreial-blog in the
future.

# The blog application  
### Add categories to the blog
I think adding some kind of categorization to the blog is important. With the 
increased number of posts the archive view will get unwieldy to browse. Introducing
categories and grouping posts under categories in the archive view will make 
things much easier in the future. 
A post should be able to have more than one category and for this reason the
relation between categories and posts should be ManyToMany.

==================================================

# Kindle Notes application  
### Administration
Currenly the only way to edit the notes in the database is through Django's
admin page. The problem with this approach is that the sheer number of notes
make it very hard to find the note you want to edit. 
The presentation of notes in the admin page could be improved but I belive that
writing a protected view for editing the notes is important because admin application
really is not the best way to handle these.
Basically the interface could be very similar to the public view for the notes.
Perhaps I could add this editing functionality right into the public view i.e.
If the user is authenticated make the notes editable. This would also give me
an opportunity to play with AJAX.

### Adding notes directly on the site
The current implementation is works just great for books that I can read on my
Kindle but I have no way of adding my highlights and notes from PDFs that I read.

- I will have to make it possible to add a new book to the database when adding 
a note. If the book I want to add a note to is not in the dropdown menu, I should
be able to just add in some more details and create the book in the databse.
Or I could just create the book via Django admin and then start adding the note/highlight.

### Export functionality for notes and highlights
While I usually don't need this for digital books, I would like to have a way of
exporting all the notes I took for a dead-tree book and print it on a piece of
paper so that I can put in between pages for future reference. This could be useful
for digital books as well. Outputting it as PDF should be pretty easy.
