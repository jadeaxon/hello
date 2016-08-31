#pragma once

// Qt
#include <QMainWindow>

// cuteedit2
#include "ui_MainWindow.h"

// Forward reference.
class QLabel;

// The main application window.
// Note how multiple inheritance is used here to get the Ui::MainWindow class created
// via Qt Designer.
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
		QLabel* mStatLabel;

}; // class MainWindow


