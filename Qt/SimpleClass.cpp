// All Qt class start with a Q prefix.
#include <QObject>
#include <QtDebug>
#include <QString>

// #define QT_NO_DEBUG_OUTPUT to turn off debug output.
// qDebug(...), qWarning(...), qFatal(...)

#include <iostream>

// Although Qt works well alongside the C++ Standard Template Library (STL), you should try to use the Qt framework
// classes as much as possible.
// #include <string>
// using std::string; // So you can say 'string' instead of 'std::string'.


// Every class in a pure Qt application directly or indirectly inherits from QObject.
class SimpleClass : public QObject {
public:
    SimpleClass(const QString& text, QObject* parent = 0);

    const QString& text() const;
    
    void setText(const QString& text);
    
    int getLengthOfText() const;

private:
    QString m_text;


}; // class SimpleClass


int main(int argc, char **argv ) {
    SimpleClass *a, *b, *c;

    a = new SimpleClass("foo" );
    b = new SimpleClass("ba-a-ar");
    c = new SimpleClass("baz");

    std::cout << a->text() << " (" << a->getLengthOfText() << ")" << std::endl;
    a->setText(b->text());
    std::cout << a->text() << " (" << a->getLengthOfText() << ")" << std::endl;

    int result = a->getLengthOfText() - c->getLengthOfText();

    // Any time an object is created, something needs to be given responsibility for destroying it.
    delete a;
    delete b;
    delete c;


    int dynamicResult = dynamicMemory();
    std::cout << result << " " << dynamicResult << std::endl;


    return 0;

} // main(...)



// Use a QObject parent to automatically delete SimpleClass instances.
int dynamicMemory() {
    // Notice that the parent is a stack object.  This way, when it goes out of scope (when this function exits), it
    // will be automatically deleted.  This will trigger it to delete the heap objects which it is a parent of.ZZ
    QObject parent;
    SimpleClass *a, *b, *c;

    a = new SimpleClass("dynamic foo", &parent);
    b = new SimpleClass("dynamic ba-a-ar", &parent);
    c = new SimpleClass("dynamic baz", &parent);
    
    qDebug() << a->text() << " (" << a->getLengthOfText() << ")";
    a->setText(b->text());
    qDebug() << a->text() << " (" << a->getLengthOfText() << ")";
    
    return a->getLengthOfText() - c->getLengthOfText();

} // dynamicMemory()


