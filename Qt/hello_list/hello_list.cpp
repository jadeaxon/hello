#include <QString>
#include <QList>
#include <QDebug>

int main() {
    QList<QString> list;
    list << "foo" << "bar" << "baz";
 
    foreach(QString s, list) {
        qDebug() << s;
    }

}


