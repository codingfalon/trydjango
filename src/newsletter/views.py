from django.shortcuts import render

# Create your views here.
def home(request):
	title = "Welcome"											#view variable 
	if request.user.is_authenticated():							#ensures user is logged in
		title = "My Title %s" %(request.user)					#instead of just rendering, gives dynamic data
	context = {
		"title": title,											#template context variable (different instance than line 5)
		"abc":123											
	}
	return render(request, "home.html", context)				#note the request/response cycle 