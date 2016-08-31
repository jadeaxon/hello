#include "Configuration.h"

// Standard C++ Library
#include <iostream>

// Qt
#include <QFile>
#include <QRegExp>
#include <QTextStream>


using namespace std;


//==============================================================================
// Constructors, Initializers, Destructor
//==============================================================================
 

// Constructs a configuration from file at given path.
Configuration::Configuration(const QString& path) {
	QFile file(path);
	if ( !file.open(QIODevice::ReadOnly) ) {
		cerr << "Failed to read config file: " << path.toUtf8().data() << endl;
		// TO DO: Throw some kind of I/O exception.
		// ::exit(1);
	}

	QTextStream in(&file);

	// Read in each key/value pair.
	while (!in.atEnd()) {
		QString line = in.readLine();    
		
		QString key;
		QString value;

		QRegExp regexp("^(.*)[=](.*)$"); // key = value
		regexp.setMinimal(true); // Non-greedy quantifiers.	
		if ( regexp.exactMatch(line) ) {
			key = regexp.cap(1).trimmed();
			value = regexp.cap(2).trimmed();
		}
		else { // Key only; no value.
			key = line.trimmed();
		}
	
	
		// Skip blank lines and comments.
		if (key.isEmpty()) { continue; }
		if (key.startsWith("#")) { continue; }

		this->map[key] = value;

	} // next line

	file.close();

} // constructor



//==============================================================================
// Public Instance Methods
//==============================================================================

// Prints out the configuration key/value pairs.
void Configuration::print() const {
	// Okay, let's see what we've read in.
	QMapIterator<QString, QString> i(this->map);
	while (i.hasNext()) {
		i.next();
		cout << i.key().toUtf8().data() << " = " << i.value().toUtf8().data() << endl;
	} // next key/value pair

}


// Retrieves the value for a key.
// Returns blank value if key not found.  Should it throw an exception?
QString Configuration::value(const QString& key) const {
	QString value = this->map.value(key, QString(""));
	return value;

}


// Retrieves the value for a key.  Synonymn for value() method.
QString Configuration::get(const QString& key) const {
	return this->value(key);
}



