from django.db import models

# Represents a language and keeps track of the votes
class Language(models.Model):

	num_votes = models.IntegerField()
	name = models.TextField()

	def vote(self):
		self.num_votes += 1