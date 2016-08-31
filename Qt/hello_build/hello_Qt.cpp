/*

To build and run:
Install libQtCore4-devel-4.5.3-1 Cygwin package.
Alias qmake-qt4 to qmake.  Or create a soft link in /usr/bin.

Not that you CANNOT use the Windows/mingw installation inside Cygwin.  Maybe you can, but I couldn't get it to work.  If
you want to use that, run under a Windows command prompt by starting C:\Users\Jade
Axon\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Qt SDK\Desktop\Qt 4.7.4 for Desktop (MinGW).lnk.
Basically, it just sets up some environment variables using qtenv2.bat (part of Qt Windows distro).

$ qmake -project
$ qmake
$ make
$ ./hello_build.exe

To start from scratch:
$ make distclean
$ rm hello_build.pro

*/


#include <QtDebug>

int main() {
    qDebug() << "Hello Qt!";
    return 0;

}

