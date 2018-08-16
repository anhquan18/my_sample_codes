import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 MessageBox'
        self.left = 40
        self.top = 40
        self.width = 600
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        '''
        self.b1 = QPushButton('Activate new GUI', self)
        self.b1.setToolTip('Just Click It')
        self.b1.move(200, 200)
        self.b1.clicked.connect(self.showDialog)

        self.show()'''
        
        buttonReply = QMessageBox.question(self, 'PyQt5 message',
            "Do you like PyQt5",
            QMessageBox.Yes | QMessageBox.Close | QMessageBox.No ,
            QMessageBox.Yes)

        if buttonReply == QMessageBox.Yes:
            self.showDialog()
            print ('Yes clicked')
        elif buttonReply == QMessageBox.No:
            print ('No clicked.')

        self.show()

        sys.exit(app.exec_())

    def showDialog(self):
        msbox = QMessageBox()
        msbox.setIcon(QMessageBox.Question)
        
        msbox.setText("New question for you:")
        msbox.setInformativeText("Do you like Python?")
        msbox.setWindowTitle("GUI after a clicked")
        msbox.setDetailedText("The details are as follow:")
        msbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Yes | QMessageBox.Retry)
        msbox.buttonClicked.connect(self.signal_exec)

        retval = msbox.exec_()
        print ("value of pressed message box's button:", retval)

    def signal_exec(self, button):
        print ("Button pressed is:", button.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
