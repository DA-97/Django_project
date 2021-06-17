from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    
    def __str__(self):
        return self.subject

class Photo(models.Model):
    post = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

class Answer(models.Model):
    voter = models.ManyToManyField(User, related_name='voter_answer')
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)