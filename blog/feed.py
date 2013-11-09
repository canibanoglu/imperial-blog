from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models import BlogPost

class LatestEntriesFeed(Feed):
    title = "The Imperial Blog"
    link = "/feed/"
    description = "Latest addition to the Imperial Blog"

    def items(self):
        return BlogPost.objects.filter(draft_status=False).order_by('-date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('blog:read_article', kwargs={'slug': item.slug})
