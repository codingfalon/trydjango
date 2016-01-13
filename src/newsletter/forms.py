from django import forms				#standard import model			

from .models import SignUp 				#imports SignUp model from newsletter application to forms.py 


class SignUpForm(forms.ModelForm):					#standard forms naming convention in Django
	model = SignUp 								#refers to sign up form (creates models based on this form)
	fields = ['email', 'full_name']				#fields in form, from models, *note use of list
	#exclude = ['full_name']					#use sparingly to exclude fields, not very specific/best method

	def clean_email(self):  						
		email = self.cleaned_data.get('email')		#get retrieves information from models/database
		email_base, provider = email.split("@")		#uses string method to categorize email parts 
		domain = provider.split('.')
		if not domain[-1].lower() == "edu":			#this method will check for the final extension (in case of multiple extensions)
			raise forms.ValidationError("Please use a valid .EDU email address") #note creation of error message
		return email 

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		firstname = full_name.split(' ')			#example of another validation technique with full name field 
		if not str(firstname).lower() == "falon":  
			raise forms.ValidationError("Your first name must be falon")
		return full_name 