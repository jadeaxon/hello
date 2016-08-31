#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

namespace Ui {
    class Widget;
}

#include "testlocalsocketipc.h"

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = 0);
    ~Widget();

private:
    Ui::Widget *ui;

public slots:
    void messageReceived(QString);
    void send_button_clicked();

private:
    LocalSocketIpcServer * m_server;
    LocalSocketIpcClient* m_client;
};

#endif // WIDGET_H
