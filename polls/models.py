from django.db import models
from django.utils import timezone
import datetime

from django.utils.functional import lazy

NEW = 'new'
INP = 'inp'
CLOSED = 'closed'
STATE_CHOICES = (
    (NEW, 'new question'),
    (INP, 'in progress'),
    (CLOSED, 'closed question'),
)

STATE_CHOICES_FOR_NEW = (
    (NEW, 'new question'),
    (INP, 'in progress'),
)


class Question(models.Model):
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=STATE_CHOICES_FOR_NEW)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
