#include <QApplication> // Main app class.  Needed for event loop.
#include <QHBoxLayout> // Horizontal box layout.
#include <QSlider> // A slider bar (like an audio fader).
#include <QSpinBox> // A mini text input with increment/decrement arrows.


// Creates a main window containing a slider and a spin box that are synced to each other.
int main(int argc, char* argv[]) {
	QApplication app(argc, argv);
	
	// Create the main window and give it a title.
	QWidget* window = new QWidget();
	window->setWindowTitle("Enter Your Age");
	
	// Make some widgets.
	QSpinBox* spinBox = new QSpinBox();
	spinBox->setRange(0, 130);
	
	QSlider* slider = new QSlider(Qt::Horizontal);
	slider->setRange(0, 130);
	
	// This is a common idiom: connecting a valueChanged event to a setter.
	QObject::connect(
		spinBox, SIGNAL(valueChanged(int)),
		slider, SLOT(setValue(int))
	);

	// Now the connection is bidirectional.  Thus, the two widgets are synced with each other.
	// For this to work, neither should emit an event when its setter is called such that it does
	// not actually change the widgets internal state.  Else feedback loop.
	QObject::connect(
		slider, SIGNAL(valueChanged(int)),
		spinBox, SLOT(setValue(int))
	);

	spinBox->setValue(35); // The slider should sync to this value.

	// A layout is used to lay out widgets in a parent widget.  The layout is relative, so
	// it should port to various devices with different resolution screens.
	QHBoxLayout* layout = new QHBoxLayout();
	// You add widgets to a layout rather than directly to a parent/container widget.
	layout->addWidget(spinBox);
	layout->addWidget(slider);

	// Then, you assign the layout to the parent/container widget.
	// You could turn this composite into a class and have a custom widget.
	// You could then reuse it in other apps.
	window->setLayout(layout);
	
	// Display the GUI.
	window->show();

	// Start the event loop.
	return app.exec();
} // main(...)


