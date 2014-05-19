from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import models
from django import template

from polls.models import Choice, UserProfile
from polls.forms import UserForm, UserProfileForm, ChoiceForm
#from polls.forms import UserForm
# Create your views here.

@login_required(login_url='/login/')
def index(request):
    course_list = Choice.objects.order_by('new_course')
    users = UserProfile.objects.all
    all_courses = request.user.choice_set.all()
    if request.user.first_name + ' ' + request.user.last_name != ' ':
        current_user = request.user.first_name + ' ' + request.user.last_name
    else:
        current_user = request.user.username
    if request.user.first_name != '':
        user_first_name = request.user.first_name
    else:
        user_first_name = request.user.username
        
    context = {'course_list': course_list, "users": users, "current_user":current_user, "all_courses":all_courses, "user_first_name":user_first_name}
    return render(request, 'polls/index.html', context)

@login_required(login_url='/login/')
def students_list(request, choice_id):
    course = get_object_or_404(Choice, pk=choice_id)
    all_students = course.courses_taking.all()
    if request.user.first_name != '':
        user_first_name = request.user.first_name
    else:
        user_first_name = request.user.username
    context = {'course': course, "all_students":all_students, "user_first_name":user_first_name}
    return render(request, 'polls/course_enrolled.html', context)



def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'polls/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required(login_url='/login/')
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def add_course(request):
    if request.user.first_name != '':
        user_first_name = request.user.first_name
    else:
        user_first_name = request.user.username
    context = RequestContext(request)
    message = ""
    if request.method == 'POST':
        form = ChoiceForm(data=request.POST)
        if form.is_valid():
            if not Choice.objects.filter(new_course=request.POST['new_course']).exists():
                form.save()
                return index(request)
            else:
                message = "Sorry, this course already exists in the list."
        else:
        	print form.errors
    
    else:
    	form = ChoiceForm()
    return render_to_response('polls/add_course.html', {'form': form, 'user_first_name': user_first_name, 'message': message, }, context)

@login_required(login_url='/login/')
def ajax_test(request):
    if request.method == 'POST' and request.is_ajax():
        match_course = request.POST.get("match_course", None)
        if match_course is None:
            return HttpResponse(None)
        all_courses = request.user.choice_set.all()
        if Choice.objects.get(id=match_course) in all_courses:
            request.user.choice_set.remove(Choice.objects.get(id=match_course))
            data = "0"
        else:
            match = Choice.objects.get(id=match_course).courses_taking.add(request.user)
            data = "1"
    return HttpResponse(data)