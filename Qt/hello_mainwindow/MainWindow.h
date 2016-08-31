#pragma once

// Qt
#include <QMainWindow>

// hello_mainwindow
#include "ui_MainWindow.h"

// Forward declaration.
class QLabel;


// Interesting.  Uses multiple inheritance.
class MainWindow : public QMainWindow, private Ui::MainWindow {
	Q_OBJECT
	public:
		MainWindow(QWidget* parent = 0);
		~MainWindow();

	protected:
		void setupActions();

	protected:
		void writeSettings();
		void readSettings();

	protected:
		bool mayDiscardDocument();
		void saveFile(const QString&);

	protected slots:
		void newFile();
		void loadFile();
		void saveFile();
		void saveFileAs();
		void undo();
		void redo();
		void copy();
		void about();
		void updateStats();

	private:
		QString mFilePath;

		// Status label used in the status bar.
		QLabel* mStatLabel;

}; // class MainWindow


