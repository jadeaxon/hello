// Qt
#include <QApplication>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QGridLayout>
#include <QLabel>


int main1(int, char**);
int main2(int, char**);


int main(int argc, char* argv[]) {
	 main2(argc, argv);
} // main(...)



int main1(int argc, char* argv[]) {
	QApplication a(argc, argv);
	
	// We put two labels into a vertical layout and then shove that layout
	// into a window.  We then display that window.
	// So, you can build GUIs as composites of widgets and layouts.
	QWidget window;
	QVBoxLayout* mainLayout = new QVBoxLayout(&window);
	// QHBoxLayou* mainLayout = new QHBoxLayou(&window);
	QLabel* label1 = new QLabel("One");
	QLabel* label2 = new QLabel("Two");
	mainLayout->addWidget(label1);
	mainLayout->addWidget(label2);
	
	// This widget gets implicitly wrapped in a window since it has no parent.
	// This causes all widgets in the composite window to become visible.
	window.show();
	
	return a.exec();
}


// Demonstrates a grid layout.
int main2(int argc, char* argv[]) {
	QApplication a(argc, argv);
	QWidget window;
	QGridLayout* mainLayout = new QGridLayout(&window);
	QLabel* label1 = new QLabel("One");
	QLabel* label2 = new QLabel("Two");
	QLabel* label3 = new QLabel("Three");
	QLabel* label4 = new QLabel("Four");
	QLabel* label5 = new QLabel("Five");
	QLabel* label6 = new QLabel("Six");
	mainLayout->addWidget(label1, 0, 0);
	mainLayout->addWidget(label2, 0, 1);
	mainLayout->addWidget(label3, 1, 0);
	mainLayout->addWidget(label4, 1, 1);
	mainLayout->addWidget(label5, 2, 0);
	mainLayout->addWidget(label6, 2, 1);
	window.show();
	return a.exec();
}

