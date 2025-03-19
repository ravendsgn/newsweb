from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name
    
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
