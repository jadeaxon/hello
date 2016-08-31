#include <QtGui>
#include "MainWindow.h"

//==============================================================================
// Constructors, Initializers, Destructor
//==============================================================================
 
MainWindow::MainWindow(QWidget* parent) : QMainWindow(parent) {
	// Since this widget inherits from QMainWindow and Ui::MainWindow, we can
	// apply our Qt Designer GUI to our own custom main window.
	this->setupUi(this);

	// Links actions to the methods they should trigger.
	this->setupActions();

	// A status bar can have temporary, normal, and permanent messages.
	// Normal and permanent messages can actually be widgets.
	mStatLabel = new QLabel;
	statusBar()->addPermanentWidget(mStatLabel);
	connect(textEdit, SIGNAL(textChanged()), this, SLOT(updateStatusBar()));
	
	// Make sure the status bar displays properly initially.
	this->updateStatusBar();
} // constructor(QWidget*)


// Links actions to the methods they should trigger.
void MainWindow::setupActions() {
	connect(action_quit, SIGNAL(triggered(bool)),
			qApp, SLOT(quit()));
	connect(action_open, SIGNAL(triggered(bool)),
			this, SLOT(loadFile()));
	connect(action_save, SIGNAL(triggered(bool)),
			this, SLOT(saveFile()));
	connect(action_saveas, SIGNAL(triggered(bool)),
			this, SLOT(saveFileAs()));

	connect(textEdit, SIGNAL(copyAvailable(bool)),
			action_copy, SLOT(setEnabled(bool)));
	connect(textEdit, SIGNAL(undoAvailable(bool)),
			action_undo, SLOT(setEnabled(bool)));
	connect(textEdit, SIGNAL(redoAvailable(bool)),
			action_redo, SLOT(setEnabled(bool)));

	connect(action_copy, SIGNAL(triggered(bool)),
			this, SLOT(copy()));
	connect(action_undo, SIGNAL(triggered(bool)),
			this, SLOT(undo()));
	connect(action_redo, SIGNAL(triggered(bool)),
			this, SLOT(redo()));

	connect(action_about, SIGNAL(triggered(bool)),
			this, SLOT(about()));
} // setupActions()


// Destroys this.
MainWindow::~MainWindow() {

}


//==============================================================================
// Slots
//==============================================================================


// Deals with case where we have a document that has never been saved yet when user
// exits.
bool MainWindow::mayDiscardDocument() {
	if (textEdit->document()->isModified()) {
		QString filename = mFilePath;
		if (filename.isEmpty()) filename = tr("Unnamed");
		if (QMessageBox::question(this, tr("Save Document?"),
					tr("You want to create a new document, but the "
						"changes in the current document '%1' have not "
						"been saved. How do you want to proceed?"), 
					tr("Save Document"), tr("Discard Changes") ))
			saveFile();
		return true;
	}
	return false;
}


// Creates a new file.
void MainWindow::newFile() {
	if (!mayDiscardDocument()) return;
	textEdit->setPlainText("");
	mFilePath = "";
}


// Loads a file into this editor.
void MainWindow::loadFile() {
	QString filename = QFileDialog::getOpenFileName(this);
	QFile file(filename);
	if (file.open(QIODevice::ReadOnly|QIODevice::Text)) {
		textEdit->setPlainText(QString::fromUtf8(file.readAll()));
		mFilePath = filename;
		statusBar()->showMessage(tr("File successfully loaded."), 3000);
	}
}


// Saves current file.
void MainWindow::saveFile() {
	if (mFilePath.isEmpty()) { 
		saveFileAs();
	}
	else { // File has already been saved to a path.
		saveFile(mFilePath);
	}
}


// Saves a file to a particular path.
void MainWindow::saveFile(const QString& name) {
	QFile file(name);
	if (file.open(QIODevice::WriteOnly|QIODevice::Text)) {
		file.write(textEdit->toPlainText().toUtf8());
		statusBar()->showMessage(tr("File saved successfully."), 3000);
	}
}


// Saves a file to a particular path.  Uses a QFileDialog to ask.
void MainWindow::saveFileAs() {
	mFilePath = QFileDialog::getSaveFileName(this);
	if(mFilePath.isEmpty()) return;
	saveFile(mFilePath);
} // saveFileAs()


void MainWindow::undo() {
	textEdit->document()->undo();
} // undo()


void MainWindow::redo() {
	textEdit->document()->redo();
} // redo()


void MainWindow::copy() {
	textEdit->copy();
} // copy()


// Displays a Help|About message box.
void MainWindow::about() {
	QMessageBox::about(
		this, 
		tr("About CuteEdit"), 
		tr(
			"CuteEdit 1.0\nA Qt application example.\n"
			"(c) 2006 Daniel Molkentin, Open Source Press"
		)
	);
} // about()


// Saves app settings/config/prefs.
// QSettings provides a cross-platform mechanism for doing this.
void MainWindow::writeSettings() {
	QSettings settings;
	settings.setValue("MainWindow/Size", size());
	settings.setValue("MainWindow/Properties", saveState());
} // writeSettings()


// Reads in app settings/config/prefs.
void MainWindow::readSettings() {
	QSettings settings;
	resize(settings.value("MainWindow/Size", sizeHint()).toSize());
	restoreState(settings.value("MainWindow/Properties").toByteArray());
} // readSettings()


// Updates the status bar.
void MainWindow::updateStatusBar() {
	QString text = textEdit->document()->toPlainText();
	int chars = text.length();
	text = text.simplified();
	int words = 0;
	words = text.count(" ");
	if (!text.isEmpty()) words++;
	QString output = tr("Characters: %1, Words: %2").arg(chars).arg(words); 
	mStatLabel->setText(output);
} // updateStatusBar()



