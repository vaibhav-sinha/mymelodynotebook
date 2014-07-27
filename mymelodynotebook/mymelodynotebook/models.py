from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
	name = models.CharField(max_length=256)
	movie = models.CharField(max_length=256,blank=True)
	artist = models.CharField(max_length=256,blank=True)
	scale = models.CharField(max_length=256,blank=True)
	tempo = models.IntegerField(blank=True,null=True)
	notation = models.CharField(max_length=256,blank=True)
	notes = models.CharField(max_length=256,blank=True)
	user = models.ForeignKey(User)


class Ref(models.Model):
	name = models.CharField(max_length=256)
	song = models.ForeignKey(Song)
	comment = models.CharField(max_length=256,blank=True)
	category = models.IntegerField()
	link = models.URLField(blank=True)
