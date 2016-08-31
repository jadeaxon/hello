# views.py is the typical place to put all your view functions.
# You use urls.py to associate a subURL within this webapp to a view function.
# A webapp will have a base URL (context) like http://<server>/<webapp>/.

# Standard Python Library
import datetime

# Django
from django.http import HttpResponse
from django.template import Template
from django.template import Context
from django.template import RequestContext
from django.template.loader import get_template
# You don't need the four imports above if you just use this mechanism.
from django.shortcuts import render_to_response

from django.db.models import Q

from django.core.mail import send_mail

from django.http import HttpResponseRedirect


# Web app
from books.models import Book
from books.forms import FeedbackForm


# This is a simple Django view function.
# It takes an HTTP request and returns an HTTP response.
# Returns current time as an HTTP response.
def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

# Same thing, but using Django template system in a rudimentary way.
def current_datetime_templatized(request):
	now = datetime.datetime.now()
	t = Template("<html><body>It is now {{ current_date }}.</body></html>")
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)

# Use Django's template loading mechanism to read the template from a file instead.
def current_datetime_templatized_by_file(request):
	now = datetime.datetime.now()
	t = get_template('current_date.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)

# Abbreviated form of same thing.
def current_datetime_concise(request):
	now = datetime.datetime.now()
	return render_to_response('current_date.html', {'current_date': now, 'concise': True})

# Lazy form of the same thing.
def current_datetime_lazy(request):
	current_date = datetime.datetime.now()
	concise = True
	# Now, we use template inheritance.  See templates/base.html.
	return render_to_response('current_date_derived.html', locals())


# A view function can take more than one args.  The first arg is always the
# HTTP requests.  The additional args are regexp subpattern matches from the
# URL pattern that triggered this function.
#
# So, in this case, 'offset' will be whatever substring was matched by the first
# capturing parens.
def hours_ahead(request, offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)


# Populates the books database.
# How would I do this in a separate import/population script not triggered
# inside the web framework?
def populate_books_database(request):
	from books.models import Publisher
	p1 = Publisher(
		name='Addison-Wesley',address='75 Arlington St.',
		city='Boston', state_province='MA', country='U.S.A.',
		website='http://www.addison-wesley.com/',
	)
	p1.save()
	
	p2 = Publisher(
		name="O'Reilly", address='10 Fawcett St.',
		city='Cambridge', state_province='MA', country='U.S.A.',
		website='http://www.oreilly.com/',
	)
	p2.save()
	return HttpResponse("Database populated.")
# end populate_books_database(request)


# Searches the books database.
def search_books(request):
	# Accesses arg q from an HTTP GET request.  These args come after the ? in the URL.
	# Second arg is default value if no q arg defined.
	# For HTML forms, you'd use request.POST instead to extract args from the HTTP POST request.
	query = request.GET.get('q', '')
	if query:
		# Q objects are used to build up a QuerySet.
		# They are like query subexpressions.
		qset = (
			Q(title__icontains=query) |
			Q(authors__first_name__icontains=query) |
			Q(authors__last_name__icontains=query)
		)
		results = Book.objects.filter(qset).distinct()
	else:
		results = []
	# else
		
	return render_to_response(
		"books/search.html", 
		{
			"results": results,
			"query": query
		}
	)
# end search_books(request)


# Responds to user feedback.
def feedback(request):
	if request.method == 'POST':
		form = FeedbackForm(request.POST) # Bound form.
	else:
		form = FeedbackForm() # Unbound form (no data yet).
	
	if form.is_valid():
		topic = form.cleaned_data['topic']
		message = form.cleaned_data['message']
		sender = form.cleaned_data['sender']

		# FAIL: I get a 'connection refused' error when trying to do this from digEcor.
		# send_mail(
			# 'Feedback from your site, topic: %s' % topic,
			# message, 
			# sender,
			# ['janderson@digecor.com']		
		# )
		
		return HttpResponseRedirect('/books/feedback/thanks/')

	# if

	
	return render_to_response(
		'feedback.html', 
		{'form': form},
		# You have to do the RequestContext thing for some sort of security reason.
		# You get a 'CSRF verification failed. Request aborted.' error if you don't.
		# It's Cross Site Request Forgery protection.
		context_instance=RequestContext(request)
	)
# end feedback(request)


# Says thank you for user feedback.
def thanks(request):
	# Normal HTML rendering condenses multiple spaces to a single space.  
	# So have to add space character explicitly.
	return HttpResponse("Thank you! &nbsp;Come again!")


