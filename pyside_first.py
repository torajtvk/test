import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

name = input("name: ")

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo " + name, "Hei " + name, "Hola " + name, "Привет " + name]

        self.button = QtWidgets.QPushButton("Click")
        self.button2 = QtWidgets.QPushButton("Click2")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(100, 100)
    widget.show()

    sys.exit(app.exec())