from django.urls import path, include
from rest_framework import routers
from .views import (
    FormViewSet,
    QuestionViewSet,
    OptionViewSet,
    ResponseViewSet,
    AnswerViewSet
)

router = routers.DefaultRouter()
router.register(r'forms', FormViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'options', OptionViewSet)
router.register(r'responses', ResponseViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
