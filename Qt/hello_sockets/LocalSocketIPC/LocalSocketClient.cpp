#include "LocalSocketClient.h"

#include <QtNetwork>
#include <QDebug>


LocalSocketClient::LocalSocketClient(QString remoteServername, QObject* parent) : QObject(parent) {
    m_socket = new QLocalSocket(this);
    m_serverName = remoteServername;

    connect(m_socket, SIGNAL(connected()), this, SLOT(socket_connected()));
    connect(m_socket, SIGNAL(disconnected()), this, SLOT(socket_disconnected()));

    connect(m_socket, SIGNAL(readyRead()), this, SLOT(socket_readReady()));
    connect(
		m_socket, SIGNAL(error(QLocalSocket::LocalSocketError)),
        this, SLOT(socket_error(QLocalSocket::LocalSocketError))
	);
}


LocalSocketClient::~LocalSocketClient() {
    m_socket->abort();
    delete m_socket;
    m_socket = NULL;
}


void LocalSocketClient::send_MessageToServer(QString message) {
    m_socket->abort();
    m_message = message;
    m_socket->connectToServer(m_serverName);
}


void LocalSocketClient::socket_connected(){
    QByteArray block;
    QDataStream out(&block, QIODevice::WriteOnly);
    out.setVersion(QDataStream::Qt_4_0);
    out << m_message;
    out.device()->seek(0);
    m_socket->write(block);
    m_socket->flush();
}


void LocalSocketClient::socket_disconnected() {
    qDebug() << "socket_disconnected";
}


void LocalSocketClient::socket_readReady() {
    qDebug() << "socket_readReady";
}


void LocalSocketClient::socket_error(QLocalSocket::LocalSocketError error) {
    qDebug() << "socket_error";
	qDebug() <<  error;
}





