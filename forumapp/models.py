from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	question=models.CharField(max_length=100)
	timestamp=models.DateTimeField()
	def __str__(self):
		return self.question

class Answer(models.Model):
	answer=models.CharField(max_length=100)
	timestamp=models.DateTimeField()
	question=models.ForeignKey(Question,on_delete=models.CASCADE,null=True,blank=True)
	author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	upvotes=models.IntegerField()
	def __str__(self):
		return self.answer

class Upvote(models.Model):
	reader=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	answer=models.ForeignKey(Answer,on_delete=models.CASCADE,null=True,blank=True)
		
		
		
