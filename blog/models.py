from django.db import models
from django.utils.text import slugify

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    comments_enabled = models.BooleanField(default=True)
    draft_status = models.BooleanField(default=True)
    hacker_news_link = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __unicode__(self):
        return "<BlogPost: %s>" % self.title

