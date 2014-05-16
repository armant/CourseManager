from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Choice
# Create your views here.

def index(request):
	output = '\n'.join([p.choice_text for p in Choice.objects.all()])
	return HttpResponse(output)

def students_list(request, choice_id):
	return HttpResponse("You're looking at the list of students enrolled in %s." % choice_id)