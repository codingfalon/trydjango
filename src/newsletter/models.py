from django.db import models

# Create your models here								#class represents actions of the function, note naming convention for SignUp
class SignUp(models.Model):								#models create structure similar to columns in excel spreadsheet
	email = models.EmailField()							#email field represents the type of data correlating to email variable, note email validator 
	full_name = models.CharField(max_length=120, blank=True, null=True)		#must have max_length for charfield 
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) #collects data when information is added, never changed
	updated = models.DateTimeField (auto_now_add=False, auto_now=True)	#collects data when information changes, note difference from timestamp 

	def __unicode__(self):   #__str___  use this method in python 3
		return self.email    #displays email in the database, unicode is a necessary feature 


