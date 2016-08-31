#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

    m_client = new LocalSocketIpcClient("Client1", this);
    m_server = new LocalSocketIpcServer("Client2", this);
    connect(m_server, SIGNAL(messageReceived(QString)), this, SLOT(messageReceived(QString)));
    connect(ui->pushButtonSend, SIGNAL(clicked()), this, SLOT(send_button_clicked()));
}

Widget::~Widget()
{
    delete ui;
}

void Widget::send_button_clicked()
{
    QDateTime localDateTime = QDateTime::currentDateTime();
    QString timeString = "Client2" + localDateTime.toString("hh:mm:ss AP dd/MM/yyyy");
    m_client->send_MessageToServer(timeString);
}


void Widget::messageReceived(QString message)
{
    ui->textBrowser->append(message);
}
