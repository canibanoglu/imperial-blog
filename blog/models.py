from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    @property
    def get_posts(self):
        return BlogPost.objects.filter(category=self)

    @property
    def post_count(self):
        return BlogPost.objects.filter(category=self).count()

    def __unicode__(self):
        return "<Category: %s>" % self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    comments_enabled = models.BooleanField(default=True)
    draft_status = models.BooleanField(default=True)
    hacker_news_link = models.URLField(blank=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField()
    description = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(Category, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __unicode__(self):
        return "<BlogPost: %s>" % self.title

