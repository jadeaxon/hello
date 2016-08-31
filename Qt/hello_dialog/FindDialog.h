#ifndef FINDDIALOG_H
#define FINDDIALOG_H
// Prevent multiple inclusion of this header file.

#include <QDialog> // Needed since we are inheriting from this class.

// Forward refs so we can use pointers to these types of objects.
// Using these instead of includes makes compilation faster.
class QCheckBox;
class QLabel;
class QLineEdit;
class QPushButton;


// QDialog is the base class for all dialog widgets.
class FindDialog : public QDialog {
	Q_OBJECT // Qt macro needed for signals and slots.
	public:
		// All QObjects have a parent.  The parent is responsible for deleting its children.
		// 0 is the null pointer in C++.
		FindDialog(QWidget* parent = 0);
	
	// Signals are internal events emitted by an object.
	// You can connect a signal to a slot on any other object (if arg lists match).
	signals:
		// Qt::CaseSensitivity is an enum defined in the Qt:: namespace.
		void findNext(const QString& str, Qt::CaseSensitivity cs);
		void findPrevious(const QString& str, Qt::CaseSensitivity cs);

	// A slot is just a regular method that can be triggered by a signal.
	private slots:
		void findClicked();
		void enableFindButton(const QString& text);
	
	private:
		// Component widgets of this custom composite widget.
		QLabel* label;
		QLineEdit* lineEdit;
		QCheckBox* caseCheckBox;
		QCheckBox* backwardCheckBox;
		QPushButton* findButton;
		QPushButton* closeButton;

};
#endif


