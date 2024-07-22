
import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QPushButton, QLabel, QVBoxLayout

class AppDemo(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Input Example with QLineEdit')
        self.setGeometry(500, 500, 200, 200)

        self.layout = QHBoxLayout()
        self.vlayout = QVBoxLayout()

        self.upper_label = QLabel(self)
        self.upper_label.setText('enter your number')
        self.layout.addWidget(self.upper_label)

        self.inputField_1 = QLineEdit(self)
        self.layout.addWidget(self.inputField_1)

        self.button1 = QPushButton('+', self)
        self.button1.setFixedSize(60, 60)
        self.button1.clicked.connect(self.jam)
        self.vlayout.addWidget(self.button1)

        self.button2 = QPushButton('-', self)
        self.button2.setFixedSize(60, 60)
        self.button2.clicked.connect(self.tafrigh)
        self.vlayout.addWidget(self.button2)

        self.button3 = QPushButton('/', self)
        self.button3.clicked.connect(self.taghsim)
        self.vlayout.addWidget(self.button3)

        self.button4 = QPushButton('*', self)
        self.button4.clicked.connect(self.zarb)
        self.vlayout.addWidget(self.button4)

        self.layout.addWidget(self.vlayout)

        self.inputField_2 = QLineEdit(self)
        self.layout.addWidget(self.inputField_2)

        self.resultLabel = QLabel(self)
        self.layout.addWidget(self.resultLabel)

        self.setLayout(self.layout)

    def jam(self):
        input_text_1 = int(self.inputField_1.text())
        input_text_2 = int(self.inputField_2.text())
        self.resultLabel.setText(f'You result is: {input_text_1 + input_text_2}')
    
    def tafrigh(self):
        input_text_1 = int(self.inputField_1.text())
        input_text_2 = int(self.inputField_2.text())
        self.resultLabel.setText(f'You result is: {input_text_1 - input_text_2}')

    def taghsim(self):
        input_text_1 = int(self.inputField_1.text())
        input_text_2 = int(self.inputField_2.text())
        self.resultLabel.setText(f'You result is: {input_text_1 / input_text_2}')

    def zarb(self):
        input_text_1 = int(self.inputField_1.text())
        input_text_2 = int(self.inputField_2.text())
        self.resultLabel.setText(f'You result is: {input_text_1 * input_text_2}')


app = QApplication(sys.argv)
demo = AppDemo()
demo.show()

sys.exit(app.exec_())