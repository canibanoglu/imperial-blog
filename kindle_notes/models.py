from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=750)
    author = models.CharField(max_length=750)
    image = models.URLField(blank=True, default="http://placehold.it/300x400")

    def __unicode__(self):
        return self.title + " -- " + self.author


class Note(models.Model):
    date = models.DateTimeField()
    highlight = models.TextField()
    note = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    page = models.CharField(max_length=100, blank=True)
    book = models.ForeignKey('Book')

    def __unicode__(self):
        return "<Note: from %s on %s>" % (self.book.title[:30], self.date)


