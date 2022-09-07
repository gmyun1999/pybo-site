from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list,10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        answer = form.save(commit=False)
        answer.question_id = question_id
        answer.create_date = timezone.now()
        answer.author = request.user
        answer.save()
        return redirect('pybo:detail' , question_id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')


def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form})
