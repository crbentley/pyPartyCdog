from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
# These arrays pertain specifically to class User
degree_choices = (('bachelor of science', 'BACHELOR OF SCIENCE'), ('master of science', 'MASTER OF SCIENCE'), ('doctrate of science', 'DOCTRATE OF SCIENCE'))
major_choices = (('computer science', 'COMPUTER SCIENCE'),('more majors coming soon', 'MORE MAJORS COMING SOON'))
general_classtaken_choices = (('gen1000', 'GEN 1000'),('gen1200', 'GEN 1200'))
core_classtaken_choices = (('csci4350', 'CSCI 4350'), ('csci4500', 'CIST 4500'))
core_extension_classtaken_choices = (('math3100', 'MATH 3100'),('csci4750', 'CSCI 4750'))


class User(models.Model):
    email = models.CharField(max_length=75)
    degreetrack = models.CharField(max_length=50, choices=degree_choices, default='bachelor of science')
    major = models.CharField(max_length=50, choices=major_choices, default='computer science')
    general_classtaken = MultiSelectField(choices=general_classtaken_choices, max_choices=100, max_length=100)
    core_classtaken = MultiSelectField(choices=core_classtaken_choices, max_choices=100, max_length=100)
    core_extension_classtaken = MultiSelectField(choices=core_extension_classtaken_choices, max_choices=100, max_length=100)
    def __str__(self):
        return self.email

class UserCompleted(models.Model):
    user = models.IntegerField() # how to get the id from user as its own field
    coursenumber = models.CharField(max_length=75)
    def ___str___(self):
        return self.coursenumber

class PossibleDegrees(models.Model):
    degree = models.CharField(max_length=10)
    major = models.CharField(max_length=75)
    def ___str___(self):
        return self.degree + " in " + self.major


class RequirementCategories(models.Model):
    #how to get id
    core = models.IntegerField()
    corenumbercredits = models.IntegerField()
    english = models.IntegerField()
    englishnumbercredits = models.IntegerField()
    math = models.IntegerField()
    mathnumbercredits = models.IntegerField()
    speech = models.IntegerField()
    speechnumbercredits = models.IntegerField()
    # add as needed?
    def ___str___(self):
        return "yay!"

class Course(models.Model):
    coursename = models.CharField(max_length=75)
    coursenumber = models.CharField(max_length=75)
    semesteravailable = models.CharField(max_length=1) #A for all, S for spring, F for fall
    numbercredits = models.IntegerField()
    def ___str___(self):
        return self.coursenumber

class CoursePrereqs(models.Model):
    coursenumber = models.ForeignKey('Course', on_delete=models.CASCADE,)
    def ___str___(self):
        return self.coursenumber



###########################3



class CoreCourse(models.Model):
    coursenumber = models.ForeignKey('Course', on_delete=models.CASCADE,)
    def ___str___(self):
        return self.coursenumber

class EnglishCourse(models.Model):
    coursenumber = models.ForeignKey('Course', on_delete=models.CASCADE,)
    def ___str___(self):
        return self.coursenumber

class MathCourse(models.Model):
    coursenumber = models.ForeignKey('Course', on_delete=models.CASCADE,)
    def ___str___(self):
        return self.coursenumber

class SpeechCourse(models.Model):
    coursenumber = models.ForeignKey('Course', on_delete=models.CASCADE,)
    def ___str___(self):
        return self.coursenumber
