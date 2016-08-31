#pragma once

#include <QWidget>

namespace Ui {
    class Widget;
}

#include "LocalSocketClient.h"
#include "LocalSocketServer.h"


class Widget : public QWidget {
    Q_OBJECT

	public:
		explicit Widget(QWidget* parent = 0);
		~Widget();

	protected slots:
		void send_button_clicked();
		void messageReceived(QString message);

	private:
		Ui::Widget* ui;

	private:
		LocalSocketClient* m_client;
		LocalSocketServer* m_server;
};

