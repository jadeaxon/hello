#pragma once

#include <QObject>
#include <QtNetwork>


class LocalSocketServer: public QObject {
		Q_OBJECT
	public:
		LocalSocketServer(QString servername, QObject* parent);
		~LocalSocketServer();

	signals:
		void messageReceived(QString);

	public slots:
		void socket_new_connection();

	private:
		QLocalServer*       m_server;
};


