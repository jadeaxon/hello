#pragma once

#include <QObject>
#include <QtNetwork>


class LocalSocketClient : public QObject {
    Q_OBJECT
	public:
		LocalSocketClient(QString remoteServername, QObject* parent = 0);
		~LocalSocketClient();

	signals:

	public slots:
		void send_MessageToServer(QString message);

		void socket_connected();
		void socket_disconnected();

		void socket_readReady();
		void socket_error(QLocalSocket::LocalSocketError);

	private:
		QLocalSocket*   m_socket;
		quint16         m_blockSize;
		QString         m_message;
		QString         m_serverName;
};

