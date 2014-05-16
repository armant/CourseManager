from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from polls.models import Choice
# Create your views here.

def index(request):
	course_list = Choice.objects.order_by('choice_text')
	#template = loader.get_template('polls/index.html')
	context = {'course_list': course_list}
	return render(request, 'polls/index.html', context)

def students_list(request, choice_id):
	course = get_object_or_404(Choice, pk=choice_id)
	return render(request, 'polls/course_enrolled.html', {'course': course})