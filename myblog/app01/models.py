from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    author_id = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

class ArticleAuthor(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    gener = models.CharField(max_length=10)
    age = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(ArticleAuthor, on_delete=models.CASCADE)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)