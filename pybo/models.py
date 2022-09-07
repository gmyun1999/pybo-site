from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE )
    subject = models.CharField(max_length=20)
    content = models.TextField()
    create_date = models.DateTimeField()

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
