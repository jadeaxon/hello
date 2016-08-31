#include <QApplication>
#include <QVBoxLayout>
#include <QLabel>
#include <QSpinBox>
#include <QSlider>


// Demonstrates a spinbox, a slider, and a label all staying synced to same value
// as a user interacts with them.
int main(int argc, char* argv[]) {
	QApplication a(argc, argv);
	
	// Main widget is on the stack.
	QWidget window;
	
	// All other widgets created on the heap.
	QVBoxLayout* mainLayout = new QVBoxLayout(&window);
	QLabel* label = new QLabel("0");
	QSpinBox* spinBox = new QSpinBox;
	QSlider* slider = new QSlider(Qt::Horizontal);
	
	// When you add a widget to a layout, the layout becomes the widget's parent.
	mainLayout->addWidget(label);
	mainLayout->addWidget(spinBox);
	mainLayout->addWidget(slider);
	
	// Sync label to spinbox.
	QObject::connect(
		spinBox, SIGNAL(valueChanged(int)),
		label, SLOT(setNum(int))
	);
	// Sync slider to spinbox.
	QObject::connect(
		spinBox, SIGNAL(valueChanged(int)),
		slider, SLOT(setValue(int))
	);
	// Sync label to slider.
	QObject::connect(
		slider, SIGNAL(valueChanged(int)),
		label, SLOT(setNum(int))
	);
	// Sync spinbox to slider.
	QObject::connect(
		slider, SIGNAL(valueChanged(int)),
		spinBox, SLOT(setValue(int))
	);
	
	window.show();
	
	return a.exec();
} // main(...)


