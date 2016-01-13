from django.contrib import admin

# Register your models here.
from .forms import SignUpForm 				#imports SignUpForms from newsletter/forms.py, note imports are in alphabetical order 
from .models import SignUp    				#calls SignUp class from newsletter app/models file
#from otherapp.models import OtherModel		#would link another model from another application into admin.py
class SignUpAdmin(admin.ModelAdmin):		#creates another model within admin.py
	list_display = ["__unicode__", "timestamp", "updated"]	#code matches fields in SignUp class 
	form = SignUpForm 						#establishes which form to pull data from
	#class Meta:
	#	model = SignUp        				#uses SignUp class to create model regarding logins/admin portal (displays more info)
	

admin.site.register(SignUp, SignUpAdmin)	#takes in multiple attributes 