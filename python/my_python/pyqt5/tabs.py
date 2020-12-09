import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QIcon


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabs'
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 500

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout()

        #Initial tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(100, 100)


        #Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")

        #Create First Tab
        self.tab1.layout = QVBoxLayout(self)
        self.b1 = QPushButton("PyQt5 WooHoo")
        self.b1.clicked.connect(self.on_click)
        self.tab1.layout.addWidget(self.b1)
        self.tab1.setLayout(self.tab1.layout)

        #Second Tab
        self.tab2.layout = QVBoxLayout(self)
        self.b2 = QPushButton("Ask and Answer")
        self.b2.clicked.connect(self.clicked2)
        self.tab2.layout.addWidget(self.b2)
        self.tab2.setLayout(self.tab2.layout)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def on_click(self):
        print("WOO HOO")

    def clicked2(self):
        print ("YAY")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
