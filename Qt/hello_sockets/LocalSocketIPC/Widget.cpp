#include "Widget.h"
#include "ui_widget.h"

#include <QDateTime>


Widget::Widget(QWidget* parent) : QWidget(parent), ui(new Ui::Widget) {
    ui->setupUi(this);

	// Does this really start new processes?
    m_client = new LocalSocketClient("server", this);
    m_server = new LocalSocketServer("server", this);

    connect(m_server, SIGNAL(messageReceived(QString)), this, SLOT(messageReceived(QString)));

    connect(ui->pushButtonSend, SIGNAL(clicked()), this, SLOT(send_button_clicked()));
}


Widget::~Widget() {
    delete ui;
}


// Triggered when you click the send button.  Sends a datestamp to the Unix socket server.
void Widget::send_button_clicked() {
    QDateTime localDateTime = QDateTime::currentDateTime();
    QString timeString = "client: " + localDateTime.toString("hh:mm:ss AP dd/MM/yyyy");
    m_client->send_MessageToServer(timeString);
}


// The server should echo the message back.  We then display it in a text box.
void Widget::messageReceived(QString message) {
    ui->textBrowser->append(message);
}
