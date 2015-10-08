from django.shortcuts import get_object_or_404, render

#from django.template import loader, RequestContext

#from django.http import HttpResponse

from .models import Question, Choice

from django.http import Http404


# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	#template = loader.get_template('polls/index.html')
	#context = RequestContext(request, {'latest_question_list':latest_question_list,})
	#output = ', '.join([p.question_text for p in latest_question_list])
	#return HttpResponse(output)
	#return HttpResponse(template.render(context))
	return render(request, 'polls/index.html', context)


def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	#return HttpResponse("This is the detail view of the question: %s" % question_id)
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question doesn't exist.")
	#else:
	return render(request, 'polls/detail.html' ,{'question':question})

def results(request, question_id):
	return HttpResponse("These are the results of the question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("Vote on question: %s" % question_id)