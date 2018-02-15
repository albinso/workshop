from django.db import models

# Create your models here.
class Language(models.Model):

	num_votes = models.IntegerField()
	name = models.TextField()

	def vote(self):
		self.num_votes += 1