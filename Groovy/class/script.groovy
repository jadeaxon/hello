#!/usr/bin/env groovy

// The Book class in the same directory is automatically imported.
// Is this because the class and the file have the same name and it's in the same directory?

// Define a function outside a class.
// If I try to define this in Book.groovy outside the class, the compiler blows up.
String getTitleBackwards(book) {
	title = book.getTitle()
	return title.reverse() // Some automagic imports allow this.

}

Book gina = new Book('Groovy in Action')
assert gina.getTitle() == 'Groovy in Action'
assert getTitleBackwards(gina) == 'noitcA ni yvoorG'

