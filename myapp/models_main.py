from django.db import models 
from django.contrib.auth.models import User
from time import time


def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)


class Article(models.Model):
	title = models.CharField(max_length = 200)
	createdby = models.ForeignKey(User)
	category = models.CharField(max_length= 200)
	pub_date = models.DateTimeField('Date Published')
	thumbnail = models.FileField(upload_to = get_upload_file_name)
	likes = models.IntegerField(default=0)



class Comment(models.Model):
	name = models.CharField(max_length= 200)
	pub_date = models.DateTimeField('Date Published')
	body = models.TextField()
	article = models.ForeignKey(Article)










