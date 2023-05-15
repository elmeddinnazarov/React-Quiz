# from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from quizApp import models
from . import serializers


class QuestionViewSet(ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer


class OptionViewSet(ModelViewSet):
    queryset = models.Option.objects.all()
    serializer_class = serializers.OptionSerializer


class ReportViewSet(ModelViewSet):
    queryset = models.Report.objects.all()
    serializer_class = serializers.ReportSerializer

class QuizViewSet(ModelViewSet):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer