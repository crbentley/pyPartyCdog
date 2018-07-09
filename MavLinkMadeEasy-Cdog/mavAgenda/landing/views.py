from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import User
from .models import UserCompleted
from .models import PossibleDegrees
from .models import RequirementCategories
from .models import Course
from .models import CoursePrereqs
from .models import CoreCourse
from .models import EnglishCourse
from .models import MathCourse
from .models import SpeechCourse

from .forms import UserForm

#def selectdegree(request):
    #return render(request, 'landing/selectdegree.html')

def login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.degreetrack = ""
            user.major = ""
            user.classtaken = ""
            user.save()
    else:
        form = UserForm()
        
    return render(request, 'landing/login.html', {'form': form})



def selectcourses(request):
    return render(request, 'landing/selectcourses.html')

def schedule(request):
    return render(request, 'landing/schedule.html')

def createuser(request):
    return render(request, 'landing/createuser.html')




