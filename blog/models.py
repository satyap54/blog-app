from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add = True)
	date_updated = models.DateTimeField(null = True, blank = True)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	is_updated_once = models.BooleanField(default = False)
	
	def get_absolute_url(self):
		return reverse('blog:post_detail', kwargs = {'pk' : self.pk})
