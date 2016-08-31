# This file maps incoming URLs to view functions in views.py.

from django.conf.urls import patterns, include, url

# Import our view functions from views.py.
from hello_django.views import current_datetime
from hello_django.views import current_datetime_templatized
from hello_django.views import current_datetime_templatized_by_file
from hello_django.views import current_datetime_concise
from hello_django.views import current_datetime_lazy
from hello_django.views import hours_ahead
from hello_django.views import populate_books_database
from hello_django.views import search_books
from hello_django.views import feedback
from hello_django.views import thanks


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


# We create a list of regular expressions that map to view functions.
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello_django.views.home', name='home'),
    # url(r'^hello_django/', include('hello_django.foo.urls')),

	url(r'^hello_django/$', current_datetime),
	url(r'^hello_django/template/$', current_datetime_templatized),
	url(r'^hello_django/template_by_file/$', current_datetime_templatized_by_file),
	url(r'^hello_django/concise/$', current_datetime_concise),
	url(r'^hello_django/lazy/$', current_datetime_lazy),

	url(r'^books/populate/$', populate_books_database),
	url(r'^books/search/$', search_books),
	url(r'^books/feedback/$', feedback),
	url(r'^books/feedback/thanks/$', thanks),

	# By using regexps, we can effectively extract args from any URL.
	# We capture a subpattern with parens.
	url(r'^hello_django/plus/(\d{1,2})/$', hours_ahead),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) # urlpatterns



