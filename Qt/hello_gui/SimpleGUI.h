#include <QString>
#include <QObject>

class SimpleGUI : public QObject {
    Q_OBJECT
    // The Q_OBJECT macro does some special Qt infrastructure setup.

public:
    SimpleGUI(const QString &text, QObject *parent = 0);
    const QString& text() const;
    const QString& getText() const;    
    int getLengthOfText() const;
    

public slots:
    // A slot is an event/message listener.
    void setText(const QString &text);

// The signals section cannot be declared public.
// You do not define implementations for signals.  Just define the function signature and Qt does the rest.
signals:
    // A signal is an event/message broadcaster.
    void textChanged(const QString&);

private:
    QString m_text;

}; // class SimpleGUI


