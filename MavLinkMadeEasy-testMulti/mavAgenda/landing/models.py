from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
# These arrays pertain specifically to class User
degree_choices = (('bachelor of science', 'BACHELOR OF SCIENCE'), ('master of science', 'MASTER OF SCIENCE'), ('doctrate of science', 'DOCTRATE OF SCIENCE'))
major_choices = (('computer science', 'COMPUTER SCIENCE'),('more majors coming soon', 'MORE MAJORS COMING SOON'))
general_classtaken_choices = (('gen1000', 'GEN 1000'),('gen1200', 'GEN 1200'))
core_classtaken_choices = (('csci4350', 'CSCI 4350'), ('csci4500', 'CIST 4500'))
core_extension_classtaken_choices = (('math3100', 'MATH 3100'),('csci4750', 'CSCI 4750'))


############################################################################


class User(models.Model):
    email = models.CharField(max_length=75)
    degreetrack = models.CharField(max_length=50, choices=degree_choices, default='bachelor of science')
    major = models.CharField(max_length=50, choices=major_choices, default='computer science')
    # add concentration
    #degree = models.ForeignKey('Degree', on_delete=models.PROTECT)

    #class Meta:
        #ordering = ['degree']
    
    #def __str__(self):
    #    return "%s | %s" % (self.degree, self.email)
    def __str__(self):
        return "%s" % self.email



class UserCompleted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #coursenumber = models.ForeignKey('Course', on_delete=models.CASCADE)
    general_classtaken = MultiSelectField(choices=general_classtaken_choices, max_choices=100, max_length=100)
    core_classtaken = MultiSelectField(choices=core_classtaken_choices, max_choices=100, max_length=100)
    core_extension_classtaken = MultiSelectField(choices=core_extension_classtaken_choices, max_choices=100, max_length=100)
    
    def __str__(self):
        return self.coursenumber



