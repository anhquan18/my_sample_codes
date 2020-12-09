import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button- pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height =  480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button1 = QPushButton('PyQt5 button', self)
        button1.setToolTip('This is an example button')
        button1.move(200, 200) 
        button1.clicked.connect(self.on_click)

        button2 = QPushButton('Another one', self)
        button2.setToolTip('Just another button')
        button2.move(200, 400)
        button2.clicked.connect(self.b2_clicked)

        self.show()

    @pyqtSlot()
    def on_click(self):
        print ('PyQt5 button clicked')
        os.system('python3 slot.py')

    def b2_clicked(self):
        print ('It is nothing')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
