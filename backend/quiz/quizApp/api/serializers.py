from rest_framework import serializers
from quizApp import models



class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Option
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(source='question', many=True, read_only=True)
    options_data = serializers.JSONField(write_only=True)
    
    class Meta:
        model = models.Question
        fields = '__all__'
        
    def update(self, question, validated_data):
        question = question.create(content=validated_data.get('content'))
        question.options.all().delete()
        options = []
        for option_data in validated_data.get('options_data'):
            option = models.Option(
                question=question,
                answer=option_data['answer'],
                correct=option_data['correct']
            )
            options.append(option)
        models.Option.objects.bulk_create(options)
        return question
            
    def create(self, validated_data):
        question = models.Question.objects.create(content=validated_data.get('content'))
        options = []
        for option_data in validated_data.get('options_data'):
            option = models.Option(
                question=question,
                answer=option_data['answer'],
                correct=option_data['correct']
            )
            options.append(option)
        models.Option.objects.bulk_create(options)
        return question


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='quiz', many=True, read_only=True)
    
    class Meta:
        model = models.Quiz
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = models.Report
        fields = '__all__'
