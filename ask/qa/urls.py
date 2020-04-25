from django.urls import path
from . import views

urlpatterns = [
    path('', views.qa_list, name='qa_list'),
    path('login/', views.qa_list, name="login"),
    path('signup/', views.qa_list, name="signup"),
    path('question/<int:pk>/', views.question_detail, name='question'),
    path('ask/', views.ask_new_question, name="ask_new_question"),
    path('popular/', views.popular_questions, name="popular_questions"),
    path('new/', views.qa_list, name="new"),
]
