from django.db import models
#질문 인스턴스가 생기는 곳
# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

# ---------------------------------- [edit] ---------------------------------- #
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.content
            # 실제로 들어가는 내용이 content이기 때문에 qustion 으로 받지 않는다.
# ---------------------------------------------------------------------------- #

