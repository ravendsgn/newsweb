from django.shortcuts import render, get_object_or_404
from .models import News,Category
# Create your views here.
def index(request):
    ctg = Category.objects.all()
    news = News.objects.all()
    news_uzb = News.objects.filter(category_id=1)
    news_jahon = News.objects.filter(category_id=2)
    news_it = News.objects.filter(category_id=3)
    ctx = {
        'ctg':ctg,
        'news':news,
        'news_uzb':news_uzb,
        'news_jahon':news_jahon,
        'news_it':news_it
    }
    return render(request, "index.html", {"news": news, "ctg": ctg})

def detail(request, news_id):
    news = get_object_or_404(News, id = news_id )
    return render(request, "single_page.html", {"news": news})

from django.shortcuts import render

def contact(request):
    ctg = Category.objects.all()
    news = News.objects.all()
    news_uzb = News.objects.filter(category_id=1)
    news_jahon = News.objects.filter(category_id=2)
    news_it = News.objects.filter(category_id=3)
    ctx = {
        'ctg':ctg,
        'news':news,
        'news_uzb':news_uzb,
        'news_jahon':news_jahon,
        'news_it':news_it}
    return render(request, "contact.html",ctx)


def error_page(request):
    return render(request,'404.html')