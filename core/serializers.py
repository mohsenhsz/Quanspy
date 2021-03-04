from .models import Question, Answer
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    q_answers = serializers.SerializerMethodField()
    
    def get_q_answers(self, obj):
        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'