#include <QWidget>

class EventWidget : public QWidget {
	Q_OBJECT
	public:
		EventWidget(QWidget* parent = 0);

	// When this widget receives any event, it will send out a signal.
	// Signals are internal events generated in response to external events (or other signals).
	signals:
		void gotEvent(const QString&);
	
	// Event handlers.  Notice they are not slots.
	// Events are not signals.  They are external events forwarded by the main
	// event loop running in the QApplication instance.
	protected:
		void closeEvent(QCloseEvent* event);
		void contextMenuEvent(QContextMenuEvent* event);
		void enterEvent(QEvent* event);
		void focusInEvent(QFocusEvent* event);
		void focusOutEvent(QFocusEvent* event);
		void hideEvent(QHideEvent* event);
		void keyPressEvent(QKeyEvent* event);
		void keyReleaseEvent(QKeyEvent* event);
		void leaveEvent(QEvent* event);
		void mouseDoubleClickEvent(QMouseEvent* event);
		void mouseMoveEvent(QMouseEvent* event);
		void mousePressEvent(QMouseEvent* event);
		void mouseReleaseEvent(QMouseEvent* event);
		void paintEvent(QPaintEvent* event);
		void resizeEvent(QResizeEvent* event);
		void showEvent(QShowEvent* event);
		void wheelEvent(QWheelEvent* event);

};


