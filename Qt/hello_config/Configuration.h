#pragma once

// Qt
#include <QMap>

// Reads in a configuration file of string key/value pairs.
// Assumes = separates keys from values.
// A line with no = is assumed to be a key with a "" (empty) value.
// Assumes blank lines ignored.
// Assumes lines starting with # are comments.
// Assumes keys cannot contain = character.
// Assumes keys and values cannot contain comments.
class Configuration {
	public:
		// Constructs a configuration from file at given path.
		Configuration(const QString& path);

		// Retrieves the value for a key.
		QString value(const QString& key) const;
		QString get(const QString& key) const;

		// Prints out the configuration.
		void print() const;

	private:
		// The configuration we are reading from a file.
		QMap<QString, QString> map;

};


