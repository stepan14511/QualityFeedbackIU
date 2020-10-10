from django.db import models

class Question(models.Model):

    # here the types of answers are constant
    ANSWER_TYPE = (
        ("TEXT", "Answer is text"),
        ("CHOICE", "Answer is choice"),
        ("VALUE", "Answer is value"),
    )

    text = models.TextField('text')
    answer_type = models.CharField(max_length=256, choices=ANSWER_TYPE, default='TEXT')

    def __str__(self):
        return self.text

class AnswerText(models.Model):

    # this field stores the id of the question it belongs to
    # I haven't found how to intialize this field :(
    # TODO: We need find out how to initialize it.
    question_id = models.BigIntegerField('question_id')

    # field that stores the answer as text
    answer = models.TextField('answer')

    def __str__(self):
        return self.text

class AnswerChoice(models.Model):

    # this field stores the id of the question it belongs to
    # I haven't found how to intialize this field :(
    # TODO: We need find out how to initialize it.
    question_id = models.BigIntegerField('question_id')

    # here we can add our custom choices
    CHOICES = (
        ("FIRST", "First Choice"),
        ("SECOND", "Second Choice"),
        ("THIRD", "Third Choice"),
        ("FOURTH", "Fourth Choice"),
    )

    # field that stores the answer as a choice here
    answer = models.CharField('answer', max_length=256, choices=CHOICES)

    def __str__(self):
        return self.text


class AnswerValue(models.Model):

    # this field stores the id of the question it belongs to
    # I haven't found how to intialize this field :(
    # TODO: We need find out how to initialize it.
    question_id = models.BigIntegerField('question_id')

    # field that stores the answer as a value
    # max_digits and decimal_places may be changed
    answer = models.DecimalField('answer', max_digits=5, decimal_places=1)

    def __str__(self):
        return self.text