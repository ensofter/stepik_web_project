from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Question, Answer
from django.shortcuts import get_object_or_404


def qa_list(request):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '?page='
    page = paginator.page(page)
    return render(request, 'qa/questions_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

def popular_questions(request):
    questions = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = "?page="
    page = paginator.page(page)
    return render(request, 'qa/questions_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(question__id = pk)
    return render(request, 'qa/question_detail.html', {
        'question': question,
        'answers': answers,
    })
