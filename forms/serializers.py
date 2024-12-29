from rest_framework import serializers
from .models import Form, Question, Option, Response, Answer

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'form', 'text', 'question_type', 'order', 'options']

class FormSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Form
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'questions']

class AnswerSerializer(serializers.ModelSerializer):
    selected_option = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all(), required=False, allow_null=True)
    selected_options = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all(), many=True, required=False)

    class Meta:
        model = Answer
        fields = ['id', 'response', 'question', 'text', 'selected_option', 'selected_options']

class ResponseSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Response
        fields = ['id', 'form', 'submitted_at', 'answers']

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        response = Response.objects.create(**validated_data)
        for answer_data in answers_data:
            selected_options = answer_data.pop('selected_options', [])
            answer = Answer.objects.create(response=response, **answer_data)
            if selected_options:
                answer.selected_options.set(selected_options)
        return response
