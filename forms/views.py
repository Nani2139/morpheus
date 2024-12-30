from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response as DRFResponse
from django.db.models import Count
from collections import Counter
from .models import Form, Question, Option, Response, Answer
from .serializers import (
    FormSerializer,
    QuestionSerializer,
    OptionSerializer,
    ResponseSerializer,
    AnswerSerializer
)

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit objects.
    """

    def has_permission(self, request, view):
       
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_staff

class FormViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Forms.
    """
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAdminUser])
    def analytics(self, request, pk=None):
        """
        Custom action to retrieve analytics data for a specific form.
        Accessible only by admin users.
        """
        form = self.get_object()
        responses = Response.objects.filter(form=form)
        total_responses = responses.count()

        questions = form.questions.all()
        analytics_data = {
            'form_id': form.id,
            'form_title': form.title,
            'total_responses': total_responses,
            'questions': []
        }

        for question in questions:
            question_data = {
                'question_id': question.id,
                'question_text': question.text,
                'question_type': question.question_type
            }

            if question.question_type == 'dropdown':
               
                option_counts = Answer.objects.filter(response__form=form, question=question).values('selected_option__text').annotate(count=Count('selected_option')).order_by('-count')
                analytics = {item['selected_option__text']: item['count'] for item in option_counts}
                question_data['analytics'] = analytics

            elif question.question_type == 'text':
               
                all_text = Answer.objects.filter(response__form=form, question=question).values_list('text', flat=True)
                words = ' '.join(all_text).split()
                word_counts = Counter(word.lower() for word in words if len(word) >= 3) 
                top_words = word_counts.most_common(5)
                analytics = {word: count for word, count in top_words}
                question_data['analytics'] = analytics

            elif question.question_type == 'checkbox':
                
                option_counts = Answer.objects.filter(response__form=form, question=question).values('selected_options__text').annotate(count=Count('selected_options')).order_by('-count')
                analytics = {item['selected_options__text']: item['count'] for item in option_counts}
                question_data['analytics'] = analytics

          
            analytics_data['questions'].append(question_data)

        return DRFResponse(analytics_data)

class QuestionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Questions.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminOrReadOnly]

class OptionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Options.
    """
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAdminOrReadOnly]

class ResponseViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Responses.
    Allows anonymous submissions.
    """
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [permissions.AllowAny]

class AnswerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Answers.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAdminOrReadOnly]
