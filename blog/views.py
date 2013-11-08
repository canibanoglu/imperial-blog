from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import BlogPost
from django.http import HttpResponse
import markdown

# This may need to move to a helpers.py file later on
def article_first_paragraph(article):
    return article.content.split('\n\n', 2)[1]

def index(request):
    context = RequestContext(request)
    latest_articles = BlogPost.objects.filter(draft_status=False).order_by('-date')[:5]
    context_dict = {'articles': latest_articles}
    return render_to_response('blog/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    return render_to_response('blog/about.html', {}, context)

def read_article(request, slug):
    context = RequestContext(request)
    article = get_object_or_404(BlogPost, slug=slug)
    body = markdown.markdown(article.content, ['fenced_code'])
    context_dict = {'article': article}
    return render_to_response('blog/article.html', context_dict, context)

def archives(request):
    context = RequestContext(request)
    articles = BlogPost.objects.filter(draft_status=False).order_by('-date')
    context_dict = {'articles': articles}
    return render_to_response('blog/archive.html', context_dict, context)
