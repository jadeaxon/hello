#include <QThread>

// A worker thread.
class Thread : public QThread {
	Q_OBJECT
	
	public:
		Thread();
		void setMessage(const QString& message);
		void stop();

	protected:
		void run();

	private:
		QString message;

		// Causes manipulation of variable to be atomic/visible across threads.
		// This allows the main app thread to stop instances of this worker thread.	
		volatile bool stopped;
};

