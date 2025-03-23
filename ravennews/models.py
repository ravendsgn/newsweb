from django.db import models

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)  # Added default=True

    def __str__(self):
        return self.name

# News Model
class News(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from django.contrib.auth.models import User 
from django.db import models

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    news = models.ForeignKey(News, on_delete=models.CASCADE)  
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.news.title}"
