from django.urls import path, include
from . import views as api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'questions', api_views.QuestionViewSet)
router.register(r'quizes', api_views.QuizViewSet)
router.register(r'reports', api_views.ReportViewSet)

urlpatterns = [
    path('', include(router.urls))
]
