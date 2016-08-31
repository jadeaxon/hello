#include <QtGui>


// Demonstrates basic graphics drawing in Qt.
int main(int argc, char* argv[]) {
	QApplication app(argc, argv);

	// A QPixmap is a QPaintDevice subclass.
	// A QPainter can paint on any QPaintDevice subclass.
	// So, here we make a blank canvas to draw on.
	QPixmap canvas(100, 100);
	canvas.fill();

	// Make a painter to paint on our new canvas. 
	QPainter painter(&canvas);
	
	// The painter paints a picture like the turtle in Logo.
	// Like a real painter, he has different pens, brushes, and other tools at his disposal.
	painter.setRenderHint(QPainter::Antialiasing, true);
	QPen pen(Qt::blue, 2);
	painter.setPen(pen);
	QBrush brush(Qt::green);
	painter.setBrush(brush);
	painter.drawEllipse(10, 10, 80, 80);

	// Now, we put our wonderful picture in a picture frame and hang it out for display.
	QLabel frame;
	frame.setPixmap(canvas);
	frame.show();

	return app.exec();
}


