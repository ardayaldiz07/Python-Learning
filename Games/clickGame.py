import sys
from PyQt5 import QtWidgets


class window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()
    
    def initUi(self):
        self.countValue = 1
        self.count = 0
        self.writeArea = QtWidgets.QLabel("0")
        self.button = QtWidgets.QPushButton("Click here")
        self.buyButton = QtWidgets.QPushButton("+1 Click\nCost 30 click")
        self.countValueText = QtWidgets.QLabel(f"Count Value: {self.countValue}")
        self.boxes()
        self.button.clicked.connect(self.clicked)
        self.buyButton.clicked.connect(self.buy)

    def clicked(self):
        self.count += self.countValue
        self.writeArea.setText(str(self.count))
        

    def buy(self):
        if self.count - 10 >= 0:
            self.count -= 10
            self.countValue += 1
            self.writeArea.setText(str(self.count))
            self.countValueText.setText(f"Count Value: {str(self.countValue)}")
        else:
            pass
            

    def boxes(self):
        vBox = QtWidgets.QVBoxLayout()
        vBox.addWidget(self.countValueText)
        vBox.addWidget(self.button)
        vBox.addWidget(self.writeArea)
        vBox.addWidget(self.buyButton)
        vBox.addStretch()

        hBox = QtWidgets.QHBoxLayout()
        hBox.addStretch()
        hBox.addLayout(vBox)
        hBox.addStretch() 

        self.setLayout(hBox)
        self.show()


app = QtWidgets.QApplication(sys.argv)
window1 = window()



sys.exit(app.exec_())
