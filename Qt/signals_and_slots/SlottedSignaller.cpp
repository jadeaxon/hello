#include "SlottedSignaller.h"

#include <iostream>

using namespace std;

void SlottedSignaller::setText(const QString &text) {
    // Do not emit a text changed signal (event) unless the value actually changed.
    // Otherwise, you may set off an infinite feedback loop.
    if(m_text == text)
        return;
    m_text = text;
    emit textChanged(m_text);
}


const QString& SlottedSignaller::getText() const {
    return this->m_text;
}


// Constructor.
// If a default arg value is set in the header file function definition, then don't set it here again.
SlottedSignaller::SlottedSignaller(const QString &text, QObject *parent /* = 0 */) {
    m_text = text;
    
    // TO DO: Not sure where parent hooks up to.
    // Not sure parent has to do anything other than simply be a stack variable.

}


// There must be a main function else qmake makefiles chokes.
int main() {
    // The point of the parent object is that it lives on the stack and knows about its children that live on the heap.
    // Thus when the parent falls off the stack, it can automatically delete its heap children.
    QObject parent;

    // I like Class* foo syntax over Class *foo.  Doesn't work for multiple declarations on a single lines though.
    SlottedSignaller *a, *b, *c; 
    a = new SlottedSignaller("foo", &parent);
    b = new SlottedSignaller("bar", &parent);
    c = new SlottedSignaller("baz", &parent);

    cout << a->getText().toStdString() << endl;
    cout << b->getText().toStdString() << endl;
    cout << c->getText().toStdString() << endl;

    // You have this idea that the connection--the event/signal emitter to listener/slot relationship--is itself an
    // object that can be created.  Thus, you configure an application via instantiating these links.  Like wiring up
    // electronic components on a breadboard.
    //
    // Aside from connection/relationship/wire objects lending themselves to being defined in external text
    // configuration files, they achieve another useful purpose.  They completely decouple the two conneted classes.
    // The classes need not know anything about each other or even that they are connected.  This kind of decoupling at
    // a subsystem level allows you to far more easily write multiple UIs for the same abstract application.
    QObject::connect(
        a, SIGNAL(textChanged(const QString&)),
        b, SLOT(setText(const QString&)) 
    );

    QObject::connect(
        b, SIGNAL(textChanged(const QString&)),
        c, SLOT(setText(const QString&))
    );

    QObject::connect(
        c, SIGNAL(textChanged(const QString&)),
        b, SLOT(setText(const QString&))
    
    );

    // a triggers b; b triggers c; c triggers b
    // So, changing the text in a should also change b and c.
    a->setText("new text");
    
    cout << a->getText().toStdString() << endl;
    cout << b->getText().toStdString() << endl;
    cout << c->getText().toStdString() << endl;

    return 0;

} // main()


