from django.shortcuts import render

from django.http import HttpResponse

from .models import Question, Choice
# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([p.question_text for p in latest_question_list])
	return HttpResponse(output)


def detail(request, question_id):
	return HttpResponse("This is the detail view of the question: %s" % question_id)

def results(request, question_id):
	return HttpResponse("These are the results of the question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("Vote on question: %s" % question_id)