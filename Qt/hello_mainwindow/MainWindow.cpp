#include "MainWindow.h"

// Qt
#include <QLabel>


//==============================================================================
// Constructors, Initializers, Destructor
//==============================================================================
 
MainWindow::MainWindow() {
	this->setWindowTitle(tr("CuteEdit"));
	this->resize(600, 400);
	QLabel* label = new QLabel(tr("Central Widget"));
	this->setCentralWidget(label);
	label->setAlignment(Qt::AlignCenter);
}


MainWindow::MainWindow(QWidget* parent) : QMainWindow(parent) {
	// Interesting.  Since we have inherited from Ui::MainWindow, we can apply
	// the GUI to ourself.
	this->setupUi(this);
	
	this->setupActions();

	mStatLabel = new QLabel;
	
	// Status bars can have temporary, normal, and permanent messages.
	// Normal and permanent messages can be widgets.
	statusBar()->addPermanentWidget(mStatLabel);
	connect(textEdit, SIGNAL(textChanged()), this, SLOT(updateStats()));
	this->updateStats();
} // constructor(QWidget*)


// Wires up the signals and slots.
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


//==============================================================================
// Slots
//==============================================================================

void MainWindow::loadFile() {
	QString filename = QFileDialog::getOpenFileName(this);
	QFile file(filename);
	if (file.open(QIODevice::ReadOnly|QIODevice::Text)) {
		textEdit->setPlainText(QString::fromUtf8(file.readAll()));
		mFilePath = filename;
		statusBar()->showMessage(tr("File successfully loaded."), 3000);
	}
} // loadFile()


void MainWindow::saveFile() {
	if (mFilePath.isEmpty()) {
		saveFileAs();
	}
	else { // Was previously saved to a path.
		saveFile(mFilePath);
	}

} // saveFile()


void MainWindow::saveFile(const QString& name) {
	QFile file(name);
	if (file.open(QIODevice::WriteOnly|QIODevice::Text)) {
		file.write(textEdit->toPlainText().toUtf8());
		this->statusBar()->showMessage(tr("File saved successfully."), 3000);
	}
} // saveFile(const QString&)


void MainWindow::saveFileAs() {
	mFilePath = QFileDialog::getSaveFileName(this);
	if (mFilePath.isEmpty()) return;
	this->saveFile(mFilePath);
} // saveFileAs()



bool MainWindow::mayDiscardDocument() {
	if (textEdit->document()->isModified()) {
		QString filename = mFilePath;
		if (filename.isEmpty()) filename = tr("Unnamed");
		if (QMessageBox::question(this, tr("Save Document?"),
					tr("You want to create a new document, but the "
						"changes in the current document ’%1’ have not "
						"been saved. How do you want to proceed?"),
					tr("Save Document"), tr("Discard Changes") ))
			saveFile();
		return true;
	}
	return false;
} // mayDiscardDocument()


void MainWindow::newFile() {
	if (!mayDiscardDocument()) return;
	textEdit->setPlainText("");
	mFilePath = "";
} // newFile()



// Displays Help|About message box.
void MainWindow::about() {
	QMessageBox::about(
		this, 
		tr("About CuteEdit"),
		tr("CuteEdit 1.0 \nA Qt application example.\n"
		   "(c) 2006 Daniel Molkentin, Open Source Press"
		)
	);
}


// Updates the status bar.
void MainWindow::updateStats() {
	QString text = textEdit->document()->toPlainText();
	int chars = text.length();
	text = text.simplified();
	int words = 0;
	words = text.count(" ");
	if (!text.isEmpty()) words++;
	QString output = tr("Characters: %1, Words: %2").arg(chars).arg(words);
	mStatLabel->setText(output);
} // updateStats()

