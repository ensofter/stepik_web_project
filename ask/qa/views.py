from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Answer
from django.shortcuts import get_object_or_404
from .forms import AskForm, AnswerForm



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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            question = get_object_or_404(Question, pk=pk)
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
        question = get_object_or_404(Question, pk=pk)
        answers = Answer.objects.filter(question__id = pk)
        return render(request, 'qa/question_detail.html', {
            'question': question,
            'answers': answers,
            'form': form,
        })

def ask_new_question(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/add_new_question.html', {
        'form': form,
    })


