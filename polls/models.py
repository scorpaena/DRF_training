from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
	question_text = models.CharField(max_length=10)
	question_desc = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')  
	question_votes = models.IntegerField(default=0)

	def __str__(self):
		return '{} {}'.format(self.id, self.question_text)


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	gender_of_voters = models.CharField(max_length=6)
	age_of_voters = models.IntegerField(default=16)

	def __str__(self):
		return '{} {}'.format(self.id, self.choice_text)
