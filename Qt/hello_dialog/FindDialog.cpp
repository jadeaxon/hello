#include <QtGui>

#include "FindDialog.h"

// Constructs a custom dialog that could be used to search for a string.
FindDialog::FindDialog(QWidget* parent) : QDialog(parent) {
	// Wrapping string literals in tr() lets them be localized.
	// You have to provide the translations in some kind of resource bundle.
	label = new QLabel(tr("Find &what:"));
	lineEdit = new QLineEdit();
	// The buddy widget of a label will gain focus when you press the shortcut key
	// associate with that label.  Using & in label string sets shortcut key.
	label->setBuddy(lineEdit);
	caseCheckBox = new QCheckBox(tr("Match &case"));
	backwardCheckBox = new QCheckBox(tr("Search &backward"));
	findButton = new QPushButton(tr("&Find"));
	findButton->setDefault(true);
	findButton->setEnabled(false);
	closeButton = new QPushButton(tr("Close"));

	// Changing the text may enable/disable the find button.
	connect(
		lineEdit, SIGNAL(textChanged(const QString&)),
		this, SLOT(enableFindButton(const QString&))
	);

	// Clicking the find button will emit a signal.
	// This would allow you to use this dialog in a larger app.
	connect(
		findButton, SIGNAL(clicked()),
		this, SLOT(findClicked())
	);

	// Clicking the close button will close this dialog.
	// Again, allows you to wire this dialog into a real app.
	// Closing the dialog may simply hide it so that it preserves state.
	connect(
		closeButton, SIGNAL(clicked()),
		this, SLOT(close())
	);

	// We nest layouts to visually organize the widgets inside the dialog window.
	// You might use Qt Designer to lay out a custom widget rather than coding it by hand.
	QHBoxLayout* topLeftLayout = new QHBoxLayout();
	topLeftLayout->addWidget(label);
	topLeftLayout->addWidget(lineEdit);
	QVBoxLayout* leftLayout = new QVBoxLayout();
	leftLayout->addLayout(topLeftLayout);
	leftLayout->addWidget(caseCheckBox);
	leftLayout->addWidget(backwardCheckBox);
	QVBoxLayout* rightLayout = new QVBoxLayout();
	rightLayout->addWidget(findButton);
	rightLayout->addWidget(closeButton);
	rightLayout->addStretch(); // Adds an invisible spacer.
	QHBoxLayout* mainLayout = new QHBoxLayout();
	mainLayout->addLayout(leftLayout);
	mainLayout->addLayout(rightLayout);
	setLayout(mainLayout);

	// Set the title and fix the dialog height to its ideal height.
	setWindowTitle(tr("Find"));
	setFixedHeight(sizeHint().height());
} // constructor()


// Handles find button click.
void FindDialog::findClicked() { // slot
	// See whether we're doing case-sensitive or case-insensitive search.
	// Determine whether we're searching forwards or backwards.
	// Emit the appropriate signal.
	QString text = lineEdit->text();
	Qt::CaseSensitivity cs =
		caseCheckBox->isChecked() ? Qt::CaseSensitive : Qt::CaseInsensitive;
	if (backwardCheckBox->isChecked()) {
		emit findPrevious(text, cs);
	} 
	else { // Search forwards.
		// You'd connect this to your main document to tell it to highlight next match.
		emit findNext(text, cs);
	}
} // findClicked()


// Enables/disables find button depending on search text state.
void FindDialog::enableFindButton(const QString& text) { // slot
	// Enable find button if search field contains text.
	// Disable find button if search field is empty.
	findButton->setEnabled(!text.isEmpty());
}


