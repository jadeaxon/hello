TEMPLATE  = app
SOURCES   = main.cpp MainWindow.cpp
HEADERS   = MainWindow.h
FORMS     = MainWindow.ui
RESOURCES = pics.qrc

# This is where the binary exe gets built.
DESTDIR = .

QMAKE_DISTCLEAN += make.out

