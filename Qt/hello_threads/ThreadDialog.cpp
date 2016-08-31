#include "ThreadDialog.h"

// Qt
#include <QHBoxLayout>


ThreadDialog::ThreadDialog(QWidget* parent) : QDialog(parent) {
	threadA.setMessage("A");
	threadAButton = new QPushButton(tr("Start A"));
	
	threadB.setMessage("B");
	threadBButton = new QPushButton(tr("Start B"));
	
	quitButton = new QPushButton(tr("Quit"));
	quitButton->setDefault(true);
	
	connect(
		threadAButton, SIGNAL(clicked()),
		this, SLOT(startOrStopThreadA())
	);
	
	connect(
		threadBButton, SIGNAL(clicked()),
		this, SLOT(startOrStopThreadB())
	);

	// Clicking the close button will close this dialog.
    // Again, allows you to wire this dialog into a real app.
    // Closing the dialog may simply hide it so that it preserves state.
	// I believe close() is a built-in QWidget slot.
    connect(
        quitButton, SIGNAL(clicked()),
        this, SLOT(close())
    );


	QHBoxLayout* layout = new QHBoxLayout();
	layout->addWidget(threadAButton);
	layout->addWidget(threadBButton);
	layout->addWidget(quitButton);

	this->setLayout(layout);
	
} // constructor


void ThreadDialog::startOrStopThreadA() {
	if (threadA.isRunning()) {
		threadA.stop();
		threadAButton->setText(tr("Start A"));
	} 
	else {
		threadA.start();
		threadAButton->setText(tr("Stop A"));
	}
}


void ThreadDialog::startOrStopThreadB() {
	if (threadB.isRunning()) {
		threadB.stop();
		threadBButton->setText(tr("Start B"));
	} 
	else {
		threadB.start();
		threadBButton->setText(tr("Stop B"));
	}
}



// I assume this gets called as a window is closing down.
void ThreadDialog::closeEvent(QCloseEvent* event) {
	// Make sure both threads have stopped running.
	threadA.stop();
	threadB.stop();
	threadA.wait();
	threadB.wait();
	event->accept();
}


