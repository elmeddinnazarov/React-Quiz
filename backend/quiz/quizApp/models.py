from django.db import models

# Create your models here.


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(
        "Quiz", on_delete=models.PROTECT, related_name='quiz')
    content = models.TextField()
    point = models.IntegerField()
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.content


class Option(models.Model):
    question = models.ForeignKey(
        "Question", on_delete=models.CASCADE, related_name='question')
    answer = models.CharField(max_length=500)
    correct = models.BooleanField()
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.answer



class Report(models.Model):
    quiz = models.ForeignKey(
        "Quiz", on_delete=models.SET_NULL, null=True, related_name='quiz_reports')
    full_name = models.CharField(max_length=200)
    total_correct = models.IntegerField()
    total_wrong = models.IntegerField()
    score = models.IntegerField()

    def __str__(self):
        return self.full_name