from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE,)
	title = models.CharField(max_length = 100)
	body = models.TextField()
	source = models.TextField(default='None')
	likes = models.ManyToManyField(User, related_name='article_like')
	def number_of_likes(self):
		return self.likes.count()
	def __str__(self):
		return self.title