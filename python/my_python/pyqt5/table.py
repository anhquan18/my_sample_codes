import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidgetItem, QVBoxLayout, QTableWidget
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table'
        self.left = 0
        self.top = 0
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()
        
        # set layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        self.show()

    def createTable(self):
        # Make table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,0,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,1,2)"))
        self.tableWidget.setItem(0,2, QTableWidgetItem("Cell (1,2,3)"))

        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,0,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,1,2)"))
        self.tableWidget.setItem(1,2, QTableWidgetItem("Cell (2,2,3)"))

        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,0,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,1,2)"))
        self.tableWidget.setItem(2,2, QTableWidgetItem("Cell (3,2,3)"))

        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,0,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,1,2)"))
        self.tableWidget.setItem(3,2, QTableWidgetItem("Cell (4,2,3)"))

        self.tableWidget.move(10, 10)

        self.tableWidget.doubleClicked.connect(self.on_click)

    def on_click(self):
        print("\n")
        for cur_table_item in self.tableWidget.selectedItems():
            print(cur_table_item.row(), cur_table_item.column(), cur_table_item.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
