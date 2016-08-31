#include <QString>
#include <QObject>

class SlottedSignaller : public QObject {
    Q_OBJECT
    // The Q_OBJECT macro does some special Qt infrastructure setup.

	public:
		SlottedSignaller(const QString& text, QObject* parent = 0);
		const QString& text() const;
		const QString& getText() const;    
		int getLengthOfText() const;
		

	public slots:
		// A slot is an event/message listener.
		void setText(const QString& text);

		// Yes, you can have pure virtual slots.
		// virtual void overrideMe() = 0;
		// In the base class, you don't have to declare override as a slot again, but it doesn't hurt.

	// The signals section cannot be declared public.
	// You do not define implementations for signals.  Just define the function signature and Qt does the rest.
	signals:
		// A signal is an event/message broadcaster.
		void textChanged(const QString&);

	private:
		// m_ => member variable (instance variable).
		// Since Qt uses the convention of <property>() for getters instead of get<Property>() you need this.
		// (Also because variables and methods are not in distinct namespaces within a class.)
		QString m_text;

}; // class SlottedSignaller


