from django.db import models

NEW = 'new'
INP = 'inp'
CLOSED = 'closed'
STATE_CHOICES = (
    (NEW, 'new question'),
    (INP, 'in progress'),
    (CLOSED, 'closed question'),
)


# class State(models.Model):
#     question_state = models.CharField(max_length=10, choices=STATE_CHOICES)


class Question(models.Model):
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=NEW)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
