import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QListWidget,
)
from PyQt5.QtCore import Qt
from decimal import Decimal


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")

        self.main_widget = QWidget()
        self.layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setMaxLength(16)
        self.display.setFixedHeight(50)

        self.layout.addWidget(self.display)

        self.history = QListWidget()
        self.history.setFixedHeight(2 * self.display.height())
        self.layout.addWidget(self.history)

        self.buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        self.grid_layout = QGridLayout()
        for i in range(4):
            for j in range(4):
                button = QPushButton(self.buttons[i][j])
                button.setFixedSize(50, 50)
                self.grid_layout.addWidget(button, i, j)
                button.clicked.connect(self.button_clicked)

        self.layout.addLayout(self.grid_layout)

        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                expression = self.display.text()
                result = str(eval(expression))
                self.display.setText(result)
                self.history.addItem(f"{expression: <16} = {result}")
                self.history.scrollToBottom()
            except Exception:
                self.display.setText("Error")
                self.history.addItem("Error")
                self.history.scrollToBottom()
        else:
            if self.display.text() == "Error":
                self.display.clear()

            self.display.setText(self.display.text() + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
