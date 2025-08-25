import sys
from PyQt5.QtWidgets import (QApplication , QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QPushButton)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Python GUI :)")
        self.setGeometry(100,0,500,500)
        # label = QLabel("Hello",self)
        # label.setGeometry(0,0,500,100)
        # label.setStyleSheet(
        #     "color: #292929;"
        #     "background-color: #ffffff;"
        #     "font-weight: bold;"
        #     "font-style: italic;"
        #     "text-decoration: underline;"
        #
        # )
        # label.setAlignment(Qt.AlignVCenter | Qt.AlignTop)
        # label = QLabel(self)
        # label.setGeometry(0,0,20,250)
        #
        # pixmap = QPixmap("image.jpg")
        # label.setPixmap(pixmap)
        #
        # label.setScaledContents(True)
        self.initUI()

    def initUI(self):
        # centralWidget = QWidget()
        # self.setCentralWidget(centralWidget)
        # label1 = QLabel("#1",self)
        # label2 = QLabel("#2",self)
        # label3 = QLabel("#3",self)
        #
        # label1.setStyleSheet("background-color : red;")
        # label2.setStyleSheet("background-color: green;")
        # label3.setStyleSheet("background-color : blue;")
        #
        # vbox = QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # centralWidget.setLayout(vbox)
        button = QPushButton("Click me!", self) 
        button.setGeometry(150,200,200,100)
        button.setStyleSheet("font-style: 30px;")
        button.clicked.connect(self.onClick)

    def onClick(self):
        print("You clicked a button")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
