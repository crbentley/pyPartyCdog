from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import User
from .models import UserCompleted
#from .models import PossibleDegrees
#from .models import RequirementCategories
#from .models import Course
#from .models import CoursePrereqs
#from .models import CoreCourse
#from .models import EnglishCourse
#from .models import MathCourse
#from .models import SpeechCourse

from .forms import UserForm
from .forms import UserCompletedForm

#def selectdegree(request):
    #return render(request, 'landing/selectdegree.html')

def login(request):
    return render(request, 'landing/login.html')
#def get_email(request):
    # if this is a POST request we need to process the form data
    #if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = LoginForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/schedule/')

    # if a GET (or any other method) we'll create a blank form
    #else:
        #form = LoginForm()



def selectcourses(request):
    if request.method == "POST":
        form = UserCompletedForm(request.POST)
        if form.is_valid():
            courses = form.save(commit=False)
            courses.save()
            return HttpResponseRedirect(reverse('landing:schedule'))
    else:
        form = UserCompletedForm()
    return render(request, 'landing/selectcourses.html', {'form': form})

def schedule(request):
    return render(request, 'landing/schedule.html')

def createuser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            #return render(request, 'landing/selectcourses.html', {'form': form})
            return HttpResponseRedirect(reverse('landing:selectcourses'))
    else:
        form = UserForm()
    return render(request, 'landing/createuser.html', {'form': form})



