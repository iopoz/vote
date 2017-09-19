from django.db import models


class State(models.Model):
    NEW = 'new'
    INP = 'inp'
    CLOSED = 'closed'
    STATE_CHOICES = (
        (NEW, 'new question'),
        (INP, 'in progress'),
        (CLOSED, 'closed question'),
    )
    question_state = models.CharField(max_length=10, choices=STATE_CHOICES)
    #
    # def create_statuses(self, state):
    #     self.create(self, state=state)
    #
    # for state in STATE_CHOICES:
    #     create_statuses(state[1])


class Question(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=0)
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
