#include <QApplication>
#include <QPixmap>
#include <QSplashScreen>
#include <QMainWindow>

#include <QDesktopWidget>
#include <QRect>
#include <QPainter>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    // It's not clear what the : syntax means below.  Where is it loading the image from?
    // QPixmap pixmap(":/splash_screen.png");
    QPixmap pixmap("./splash_screen.png"); 
    QSplashScreen splash(pixmap);
    splash.setWindowFlags(splash.windowFlags() | Qt::WindowStaysOnTopHint);

    splash.show();
    // No event processing occurs before the main QWS window initializes.
    // app.processEvents();

    // The C sleep function is in seconds.
    sleep(5);    


    // In Qt 3 embedded (and probably 4), the splash screen approach does not work.

    // The problem is the starting up time for estabilish a connection between QWSServer init() and QWSClient (my QApplication)...
    // I solved this issue forcing a drawing a QImage using QWSServer::setDesktopBackground( QImage ), so I can see a sort of splashscreen
    // during QWSServer initialization.
    // The only drawback is you cannot have access to the same method QSplashScreen class has: i.e. Message printing, Event processing,
    // and so on...
    // But my problem is gone away: I can see a fixed image during a QT/Embedded startup.

    // The interesting thing for digemenu2 is that it is the QWS.  It doesn't use a separate default QWS.
    
    QMainWindow window;
    window.show();
    splash.finish(&window);
    
    return app.exec();

 } // main(...)


// This is another solution to the full screen opaque splash screen problem.
// Scales a source splash screen image to the full screen resolution of the display.
int main2(int argc, char *argv[]) {
    QApplication app(argc, argv);
   
    QPixmap splashSourcePixmap("./splash_screen.png");
    QDesktopWidget* desktop = QApplication::desktop();
    const QRect desktopRect = desktop->availableGeometry();
 
    QPixmap splashPixmap(desktopRect.width(), desktopRect.height());
    splashPixmap.fill(QColor("070606"));
 
    QPainter p;
    p.begin(&splashPixmap);
    QRect targetRect(
        (splashPixmap.width() - splashSourcePixmap.width()) / 2,
        (splashPixmap.height() - splashSourcePixmap.height()) / 2,
        splashSourcePixmap.width(),
        splashSourcePixmap.height()
    );
    p.drawPixmap(targetRect, splashSourcePixmap);

    p.end();
 
    QSplashScreen splash(splashPixmap);
 
    splash.showFullScreen();
 
    QMainWindow window;
    window.show();
    // window.showExpanded();
    splash.finish(&window);
 
    // Enter the main event loop.
    int returnCode = app.exec();
    return returnCode;

} // main2(...)


