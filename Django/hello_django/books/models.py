from django.db import models

# Model of a published book.

class Publisher(models.Model):
	name = models.CharField(max_length = 30)
	address = models.CharField(max_length = 50)
	city = models.CharField(max_length = 60)
	# State or province in which the city is located.
	state_province = models.CharField(max_length = 30)
	country = models.CharField(max_length = 50)
	website = models.URLField()

	# It's a good idea to add a __str__ method to all of your data model classes.
	def __str__(self):
		return self.name

	# A class can have metainformation.  This is completely optional but may be useful.
	# This bit says to always order Publisher objects by name by default.
	# Result sets from databases are typically unordered otherwise.
	class Meta:
		ordering = ["name"]

	# Enables this class to be edited by the admin interface.
	class Admin: pass


# end class Publisher


class Author(models.Model):
	salutation = models.CharField(max_length = 10)
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 40)
	email = models.EmailField()
	# A photo of the author's face.
	# You must set MEDIA_ROOT in settings.py.  This folder must be write accessible by the
	# process running Django.  The upload_to dir must be MEDIA_ROOT (or a subdir).
	headshot = models.ImageField(upload_to = '/root/public')

	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)

	# Enables this class to be edited by the admin interface.
	class Admin: pass

# end class Author


class Book(models.Model):
	title = models.CharField(max_length = 100)
	# A book has 1 or more authors.
	# An author may write one or more books.
	authors = models.ManyToManyField(Author)
	# A book has a publisher.
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()

	def __str__(self):
		return self.title

	# Enables this class to be edited by the admin interface.
	# Also allows for customization of the interface to make it more useful.
	# This changes how data is displayed and enables searching on title field.
	# TO DO: This is not actually working.  I still get the default view when looking at
	# books.  Tried restarting web server and syncdb.
	class Admin:
		list_display = ('title', 'publisher', 'publication_date')
		list_filter = ('publisher', 'publication_date')
		ordering = ('-publication_date',)
		search_fields = ('title',)


# end class Book


