from PyQt5 import QtGui, QtCore, QtWidgets
import sys

class MyLabelPixmap(QtWidgets.QLabel):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QLabel.__init__(self)
        self.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.resize(800, 600)
        self.pixmap = QtGui.QPixmap("slide2.png")
        self.setPixmap(self.pixmap)
        self.installEventFilter(self)

    def eventFilter(self, source, event):
        if (source is self and event.type() == QtCore.QEvent.Resize):
            self.setPixmap(self.pixmap.scaled(self.size()))
        return super(MyLabelPixmap, self).eventFilter(source, event)

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     window = MyLabelPixmap()
#     window.show()
#     sys.exit(app.exec_())