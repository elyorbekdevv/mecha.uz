from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import *
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.title


class Lessons(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=False)
    file = models.FileField()

    def short_content(self):
        return self.content[:200]

class Courses(models.Model):
    title = models.CharField(max_length=300, null=False, blank=True)
    description = models.TextField(null=False)
    teacher = models.CharField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/', default="default.jpg")
    lessons = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def short_description(self):
        return self.description[:200]
    
    def __str__(self):
        return f"{self.title} - {self.category}"
        
class Teacher(models.Model):
    name_surname = models.CharField(max_length=200, null=False)
    biograpy = models.TextField()
    pic = models.ImageField(default = "default_cover.jpg")

class Reviews(models.Model):
    user = models.ForeignKey(Teacher, on_delete = models.CASCADE, related_name="reviews")
    comment = models.TextField
    rate = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    created_time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.rate
    
    def short_comment(self):
        return self.comment[:200]

    def __str__(self):
        return str(self.comment)