from django.shortcuts import render
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
    return render(request,'index.html',ctx)

def detail(request):
    return render(request,'single_page.html')

def contact(request):
    return render(request,'contact.html')

def error_page(request):
    return render(request,'404.html')