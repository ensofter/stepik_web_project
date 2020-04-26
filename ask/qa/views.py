from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Answer
from django.shortcuts import get_object_or_404
from .forms import AskForm, AnswerForm, SignUpForm, LoginForm
from django.views.decorators.http import require_GET
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

@require_GET
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

@require_GET
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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
        else:
            return HttpResponse('200')
    else:
        form = AnswerForm(initial={"question": question.pk})
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

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'qa/signup.html', {
        'form': form,
        'user': request.user,
        'session': request.session,
    })

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('No')
    else:
        form = LoginForm()
    return render(request, 'qa/login.html', {
        'form': form,
        'user': request.user,
        'session': request.session,
    })

