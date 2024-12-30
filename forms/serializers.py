from rest_framework import serializers
from .models import Form, Question, Option, Response, Answer

class OptionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Option model.
    """
    class Meta:
        model = Option
        fields = ['id', 'text', 'question']
        read_only_fields = ['id']

class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Question model.
    Includes nested options.
    """
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'form', 'order', 'options']
        read_only_fields = ['id', 'order']

    def create(self, validated_data):
        """
        Override the create method to handle auto-incrementing 'order' field.
        """
        return Question.objects.create(**validated_data)

class FormSerializer(serializers.ModelSerializer):
    """
    Serializer for the Form model.
    Includes nested questions.
    """
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Form
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'questions']
        read_only_fields = ['id', 'created_at', 'updated_at']

class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Answer model.
    Handles different types of answers based on question type.
    """

    response = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = [
            'id',
            'response',
            'question',
            'text',
            'selected_option',
            'selected_options'
        ]
        read_only_fields = ['id', 'response']

    def validate(self, attrs):
        """
        Custom validation to ensure correct fields are provided based on question type.
        """
        question = attrs.get('question')
        if not question:
            raise serializers.ValidationError("Question must be provided.")

        if question.question_type == 'text':
            if not attrs.get('text'):
                raise serializers.ValidationError("Text response is required for this question type.")
        elif question.question_type == 'dropdown':
            if not attrs.get('selected_option'):
                raise serializers.ValidationError("Selected option is required for this question type.")
        elif question.question_type == 'checkbox':
            if not attrs.get('selected_options'):
                raise serializers.ValidationError("At least one selected option is required for this question type.")
        else:
            raise serializers.ValidationError("Invalid question type.")

        return attrs

class ResponseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Response model.
    Includes nested answers.
    """
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Response
        fields = ['id', 'form', 'submitted_at', 'answers']
        read_only_fields = ['id', 'submitted_at']

    def create(self, validated_data):
        """
        Override the create method to handle nested answer creation.
        """
        answers_data = validated_data.pop('answers')
        response = Response.objects.create(**validated_data)
        for answer_data in answers_data:
        
            selected_options = answer_data.pop('selected_options', [])
         
            answer = Answer.objects.create(response=response, **answer_data)
            if selected_options:
                answer.selected_options.set(selected_options)
        return response
