import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QDesktopWidget, QPushButton, QFrame
from PyQt5.QtCore import Qt

class disclaimerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SCC App")
        self.setGeometry(100, 100, 800, 500)
        self.centerBlock()

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.mainLayout)

        self.showDisclaimer()

    def showDisclaimer(self):

        self.clearLayout(self.mainLayout)

        label = QLabel("[ Disclaimer message placeholder ]", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 16px;")

        button = QPushButton("Continue", self)
        button.clicked.connect(self.showHome)

        self.mainLayout.addWidget(label)
        self.mainLayout.addWidget(button)
        self.mainLayout.setAlignment(Qt.AlignCenter)

        self.homeButton = QPushButton("Home", self)
        self.homeButton.clicked.connect(self.showHome)
        self.homeButton.setGeometry(730, 20, 50, 20)

        self.helpButton = QPushButton("?", self)
        self.helpButton.clicked.connect(self.showHelp)
        self.helpButton.setGeometry(750, 20, 20, 20)

        self.homeButton.hide()
        self.helpButton.hide()
    
    def showHome(self):

        self.clearLayout(self.mainLayout)

        self.homeButton.hide()
        self.helpButton.show()

        hLayout = QHBoxLayout()
        leftSide = QVBoxLayout()

        buttonLayout = QHBoxLayout()

        imageBox = QFrame(self)
        imageBox.setStyleSheet("background-color: gray; width: 150px; height: 150px;")
        imageBox.setMinimumSize(270, 270)
        imageBox.setMaximumSize(270, 270)

        recordsButton = QPushButton("Records", self)
        recordsButton.clicked.connect(self.showRecords)
        runButton = QPushButton("Run", self)
        recordsButton.setMaximumSize(100, 40)
        runButton.setMaximumSize(100, 40)

        buttonLayout.addWidget(recordsButton)
        buttonLayout.addWidget(runButton)

        leftSide.addWidget(imageBox)
        leftSide.addSpacing(20)
        leftSide.addLayout(buttonLayout)

        rightSide = QFrame(self)
        rightSide.setStyleSheet("background-color: blue; width: 150px; height: 300px;")
        rightSide.setMinimumSize(250, 300)

        hLayout.addLayout(leftSide)
        hLayout.addSpacing(50)
        hLayout.addWidget(rightSide)

        self.mainLayout.addLayout(hLayout)

    def showHelp(self):

        self.clearLayout(self.mainLayout)

        self.homeButton.show()
        self.helpButton.hide()

        hLayout = QHBoxLayout()

        leftBoxWidget = QWidget(self)
        midBoxWidget = QWidget(self)
        rightBoxWidget = QWidget(self)

        leftBoxWidget.setStyleSheet("background-color: lightcoral;")
        midBoxWidget.setStyleSheet("background-color: lightcoral;")
        rightBoxWidget.setStyleSheet("background-color: lightcoral;")

        leftBox = QVBoxLayout(leftBoxWidget)
        midBox = QVBoxLayout(midBoxWidget)
        rightBox = QVBoxLayout(rightBoxWidget)

        leftLabel = QLabel("Left Box", self)
        midLabel = QLabel("Middle", self)
        rightLabel = QLabel("Right", self)

        leftLabel.setAlignment(Qt.AlignCenter)
        midLabel.setAlignment(Qt.AlignCenter)
        rightLabel.setAlignment(Qt.AlignCenter)

        leftBox.addWidget(leftLabel)
        midBox.addWidget(midLabel)
        rightBox.addWidget(rightLabel)

        hLayout.addWidget(leftBoxWidget, 1)
        hLayout.addWidget(midBoxWidget, 1)
        hLayout.addWidget(rightBoxWidget, 1)

        self.mainLayout.addLayout(hLayout)

    def showRecords(self):
        self.clearLayout(self.mainLayout)

        self.homeButton.hide()
        self.helpButton.show()

        hLayout = QHBoxLayout()
        leftSide = QVBoxLayout()

        buttonLayout = QHBoxLayout()

        imageBox = QFrame(self)
        imageBox.setStyleSheet("background-color: gray; width: 150px; height: 150px;")
        imageBox.setMinimumSize(270, 270)
        imageBox.setMaximumSize(270, 270)

        resultsButton = QPushButton("Results", self)
        resultsButton.clicked.connect(self.showHome)
        runButton = QPushButton("Run", self)
        resultsButton.setMaximumSize(100, 40)
        runButton.setMaximumSize(100, 40)

        buttonLayout.addWidget(resultsButton)
        buttonLayout.addWidget(runButton)

        leftSide.addWidget(imageBox)
        leftSide.addSpacing(20)
        leftSide.addLayout(buttonLayout)

        rightSide = QFrame(self)
        rightSide.setStyleSheet("background-color: purple; width: 150px; height: 300px;")
        rightSide.setMinimumSize(250, 300)

        hLayout.addLayout(leftSide)
        hLayout.addSpacing(50)
        hLayout.addWidget(rightSide)

        self.mainLayout.addLayout(hLayout)


    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def centerBlock(self):
        frame = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        self.move(frame.topLeft())





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = disclaimerWindow()
    window.show()
    sys.exit(app.exec_())