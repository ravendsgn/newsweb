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
    return render(request, "index.html", ctx)

# News Detail Page
def detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    comments = news.comment_set.all()
     # Get top 5 most viewed news

    return render(request, "single_page.html", {
        "news": news,
        "comments": comments  # Pass popular posts separately
    })



# Contact Page
def contact(request):
    categories = Category.objects.filter(is_active=True)
    news = News.objects.all()
    ctx = {
        'categories': categories,
        'news': news,
    }
    return render(request, "contact.html", ctx)

# Error Page
def error_page(request):
    return render(request, '404.html')

# Category News Page (New Function)
def category_news(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    news_list = News.objects.filter(category=category)
    ctx = {
        'category': category,
        'news_list': news_list
    }
    return render(request, "category_news.html", ctx)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import News, Comment
from .forms import CommentForm

@login_required
def add_comment(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.news = news
            comment.save()
            return redirect('detail', news_id=news.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'news': news})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
    return redirect('detail', news_id=comment.news.id)

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')
