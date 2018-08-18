import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 text box'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        #Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 80)

        #connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message', "You typed:" + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText(" Hello World") #Set the text after you get the value from text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
