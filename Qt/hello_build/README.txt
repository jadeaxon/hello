You can't make it build right from Cygwin.
Maybe it is possible, but it has defied all my attempts so far.

Even if you call cmd inside Cygwin it still screws up.
If you generate the makefile in an actual cmd window, then it will almost build under Cygwin.  Screws up due to / and \
handling.

How does qmake know that it is running under Cygwin vs. actual Windows?  It writes different makefiles in each case.

The way to make it work is this:
- open an actual Windows command prompt
- run qtenv2.bat
- qmake -project
- add CONFIG += console to the .pro file
- qmake
- mingw32-make
- cd debug
- .\executable.exe

Once the project is built, you can run it fine under Cygwin.

