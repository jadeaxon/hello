// Qt
#include <QWidget>
#include <QPushButton>
#include <QDialog>
#include <QCloseEvent>

// App
#include <Thread.h>


// A GUI dialog to launch a couple worker threads.
class ThreadDialog : public QDialog {
	Q_OBJECT
	public:
		ThreadDialog(QWidget* parent = 0);
	
	protected:
		void closeEvent(QCloseEvent* event);
		
	private slots:
		void startOrStopThreadA();
		void startOrStopThreadB();
	
	private:
		Thread threadA;
		Thread threadB;
		QPushButton* threadAButton;
		QPushButton* threadBButton;
		QPushButton* quitButton;
};

