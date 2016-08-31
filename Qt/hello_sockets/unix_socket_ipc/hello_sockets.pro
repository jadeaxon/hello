TEMPLATE = app
TARGET = 
DEPENDPATH += .
INCLUDEPATH += .

# Include the network stuff.  Need this for QLocalSocket and QLocalServer.
QT += network

# Input
HEADERS += UnixSocketClient.h UnixSocketServer.h UnixSocketWindow.h
SOURCES += main.cpp \
           UnixSocketClient.cpp \
           UnixSocketServer.cpp \
           UnixSocketWindow.cpp
