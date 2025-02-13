import sys
import os
import csv
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QDesktopWidget, QPushButton, QFrame, QFileDialog, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QPainterPath, QPixmap

class disclaimerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SCC App")
        self.setGeometry(100, 100, 800, 500)
        self.setFixedSize(800,500)
        self.centerBlock()

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.mainLayout)

        self.showDisclaimer()

    def showDisclaimer(self):

        self.clearLayout(self.mainLayout)
        self.setStyleSheet("background-color:rgb(213, 230, 247);")

        class roundWidget(QWidget):
            def paintEvent(self, event):
                painter = QPainter(self)
                painter.setRenderHint(QPainter.Antialiasing)

                margin = 2
                rect = self.rect().adjusted(margin, margin, -margin, -margin)
                rectF = QRectF(rect)
                cornerRadius = 50

                path = QPainterPath()
                path.addRoundedRect(rectF, cornerRadius, cornerRadius)

                pen = QPen(QColor(20, 80, 120), 4)
                pen.setJoinStyle(Qt.MiterJoin)
                painter.setPen(pen)
                painter.setBrush(QBrush(Qt.white))

                painter.drawPath(path)

        roundContainer = roundWidget(self)
        roundContainer.setGeometry(50, 60, self.width() - 100, self.height() - 120)  
        self.disclaimerContainer = roundContainer 

        containerLayout = QVBoxLayout(roundContainer)
        containerLayout.setAlignment(Qt.AlignCenter)

        label = QLabel("[ Disclaimer message placeholder ]", self)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 16px;")

        button = QPushButton("Continue", self)
        button.setCursor(Qt.PointingHandCursor)
        button.clicked.connect(self.checkContinue)
        button.setStyleSheet("""
            QPushButton {
                background-color: rgb(21, 96, 130);
                color: white;
                font-weight: 800;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: rgb(12, 58, 78);
            }

        """)

        containerLayout.addWidget(label)
        containerLayout.addWidget(button)

        self.homeButton = QPushButton("Home", self)
        self.homeButton.setCursor(Qt.PointingHandCursor)
        self.homeButton.clicked.connect(self.showHome)
        self.homeButton.setGeometry(735, 20, 37, 37)
        self.homeButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(21, 96, 130);
                border-radius: 18px;
                color: white;
                font-weight: 800;
                font-size: 10px;
            }
            QPushButton:hover {
                background-color: rgb(12, 58, 78);
            }

        """)

        self.helpButton = QPushButton("?", self)
        self.helpButton.setCursor(Qt.PointingHandCursor)
        self.helpButton.clicked.connect(self.showHelp)
        self.helpButton.setGeometry(735, 20, 37, 37)
        self.helpButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(21, 96, 130);
                border-radius: 18px;
                color: white;
                font-weight: 800;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: rgb(12, 58, 78);
            }

        """)

        self.homeButton.hide()
        self.helpButton.hide()

    def checkContinue(self):
        if hasattr(self, 'disclaimerContainer'):
            self.disclaimerContainer.hide()

        self.showHome()
    
    def showHome(self):

        self.clearLayout(self.mainLayout)

        self.homeButton.hide()
        self.helpButton.show()

        hLayout = QHBoxLayout()

        leftSide = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        self.imageBox = ImageDropBox(self)

        recordsButton = QPushButton("RECORDS", self)
        recordsButton.setCursor(Qt.PointingHandCursor)
        recordsButton.clicked.connect(self.showRecords)
        recordsButton.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid black;
                border-radius: 20px;
                font-weight: 800;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }

        """)
        recordsButton.setMaximumSize(100, 40)

        runButton = QPushButton("RUN", self)
        runButton.setCursor(Qt.PointingHandCursor)
        runButton.clicked.connect(self.runCommand)
        runButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(21, 96, 130);
                border-radius: 20px;
                color: white;
                font-weight: 800;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: rgb(12, 58, 78);
            }

        """)
        runButton.setMaximumSize(100, 40)

        buttonLayout.addWidget(recordsButton)
        buttonLayout.addWidget(runButton)

        leftSide.addWidget(self.imageBox)
        leftSide.addSpacing(20)
        leftSide.addLayout(buttonLayout)

        rightSide = QFrame(self)
        rightSide.setStyleSheet("background-color: white; width: 150px; height: 150px; border: 4px solid rgb(20, 80, 120); border-radius: 20px")
        rightSide.setFixedSize(270, 350)

        hLayout.addLayout(leftSide)
        hLayout.addWidget(rightSide)

        self.mainLayout.addLayout(hLayout)

    def runCommand(self):
        self.imageBox.showLoading()

    def showHelp(self):

        self.clearLayout(self.mainLayout)

        self.homeButton.show()
        self.helpButton.hide()

        hLayout = QHBoxLayout()

        leftBoxWidget = QWidget(self)
        leftBox = QVBoxLayout(leftBoxWidget)
        leftBox.setSpacing(30)
        leftBox.setContentsMargins(0, 0, 0, 0)

        leftTopWidget = QLabel(self)
        leftTopWidget.setFixedSize(70, 70)
        leftTopWidget.setAlignment(Qt.AlignTop)
        pixmapLeft = QPixmap("pic.png")
        scaledPixmapLeft = pixmapLeft.scaled(leftTopWidget.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        leftTopWidget.setPixmap(scaledPixmapLeft)
        leftBox.addWidget(leftTopWidget, 0, Qt.AlignCenter)

        leftBottomWidget = QWidget(self)
        leftBottomWidget.setAttribute(Qt.WA_StyledBackground, True)
        leftBottomWidget.setStyleSheet(
            "background-color: white; border: 2px solid rgb(21, 96, 130); border-radius: 35px; padding: 0px; margin: 0px;"
        )
        leftBottomWidget.setFixedSize(200,200)

        leftBottomLayout = QVBoxLayout(leftBottomWidget)
        leftBottomLayout.setContentsMargins(0, 0, 0, 0)
        leftBottomLayout.setSpacing(0)

        leftLabel2 = QLabel("Upload an image with a compatible format. (JPEG, PNG)", self)
        leftLabel2.setWordWrap(True)
        leftLabel2.setAlignment(Qt.AlignCenter)
        leftBottomLayout.addWidget(leftLabel2)

        leftBox.addWidget(leftBottomWidget, 0, Qt.AlignHCenter) 

        #-----------------------------------------------------------------------------

        rightBoxWidget = QWidget(self)
        rightBox = QVBoxLayout(rightBoxWidget)
        rightBox.setSpacing(30)

        rightTopWidget = QLabel(self)
        rightTopWidget.setFixedSize(70, 70)
        rightTopWidget.setAlignment(Qt.AlignCenter) 

        pixmap = QPixmap("folder.png") 

        scaled_pixmap = pixmap.scaled(rightTopWidget.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        rightTopWidget.setPixmap(scaled_pixmap)

        rightBox.addWidget(rightTopWidget, 0, Qt.AlignCenter)

        rightBottomWidget = QWidget(self)
        rightBottomWidget.setAttribute(Qt.WA_StyledBackground, True)
        rightBottomWidget.setStyleSheet(
            "background-color: white; border: 2px solid rgb(21, 96, 130); border-radius: 35px; padding: 0px; margin: 0px;"
        )
        rightBottomWidget.setFixedSize(200,200)

        rightBottomLayout = QVBoxLayout(rightBottomWidget)
        rightBottomLayout.setContentsMargins(0, 0, 0, 0)
        rightBottomLayout.setSpacing(0)

        rightLabel2 = QLabel("Access references to results or     previous records", self)
        rightLabel2.setWordWrap(True)
        rightLabel2.setAlignment(Qt.AlignCenter)
        rightBottomLayout.addWidget(rightLabel2)

        rightBox.addWidget(rightTopWidget, 1, Qt.AlignHCenter)    
        rightBox.addWidget(rightBottomWidget, 3, Qt.AlignHCenter) 

        #---------------------------------------------------------------------------

        midBoxWidget = QWidget(self)
        midBox = QVBoxLayout(midBoxWidget)
        midBox.setSpacing(30)

        midTopWidget = QLabel(self)
        midTopWidget.setFixedSize(70, 70)
        midTopWidget.setAlignment(Qt.AlignCenter)
        pixmapMid = QPixmap("gear.png")
        scaledPixmapMid = pixmapMid.scaled(midTopWidget.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        midTopWidget.setPixmap(scaledPixmapMid)
        midBox.addWidget(midTopWidget, 0, Qt.AlignCenter)

        midBottomWidget = QWidget(self)
        midBottomWidget.setAttribute(Qt.WA_StyledBackground, True)
        midBottomWidget.setStyleSheet(
            "background-color: white; border: 2px solid rgb(21, 96, 130); border-radius: 35px; padding: 0px; margin: 0px;"
        )
        midBottomWidget.setFixedSize(200,200)

        midBottomLayout = QVBoxLayout(midBottomWidget)
        midBottomLayout.setContentsMargins(0, 0, 0, 0)
        midBottomLayout.setSpacing(0)

        midLabel2 = QLabel("Click run to start the classification process", self)
        midLabel2.setWordWrap(True)
        midLabel2.setAlignment(Qt.AlignCenter)
        midBottomLayout.addWidget(midLabel2)

        midBox.addWidget(midTopWidget, 1, Qt.AlignHCenter)    
        midBox.addWidget(midBottomWidget, 3, Qt.AlignHCenter) 

        hLayout.addWidget(leftBoxWidget,  alignment=Qt.AlignCenter)
        hLayout.addWidget(midBoxWidget,  alignment=Qt.AlignCenter)
        hLayout.addWidget(rightBoxWidget,  alignment=Qt.AlignCenter)

        self.mainLayout.addLayout(hLayout)

    def showRecords(self):
        self.clearLayout(self.mainLayout)

        self.homeButton.hide()
        self.helpButton.show()

        hLayout = QHBoxLayout()
        leftSide = QVBoxLayout()
        buttonLayout = QHBoxLayout()

        self.imageLabel = QLabel(self)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setFixedSize(270, 270)
        self.imageLabel.setStyleSheet("background-color: white; border: 4px solid rgb(20, 80, 120); border-radius: 20px; color: gray")
        self.imageLabel.setText("Click on record to see image")

        resultsButton = QPushButton("RESULTS", self)
        resultsButton.setCursor(Qt.PointingHandCursor)
        resultsButton.clicked.connect(self.showHome)
        resultsButton.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid black;
                border-radius: 20px;
                font-weight: 800;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }

        """)
        resultsButton.setMaximumSize(100, 40)

        runButton = QPushButton("RUN", self)
        runButton.setCursor(Qt.PointingHandCursor)
        runButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(21, 96, 130);
                border-radius: 20px;
                color: white;
                font-weight: 800;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: rgb(12, 58, 78);
            }

        """)
        runButton.setMaximumSize(100, 40)

        buttonLayout.addWidget(resultsButton)

        leftSide.addWidget(self.imageLabel)
        leftSide.addSpacing(20)
        leftSide.addLayout(buttonLayout)

        rightSide = QFrame(self)
        rightSide.setStyleSheet("background-color: white; width: 150px; height: 150px; border-radius: 20px")
        rightSide.setFixedSize(270, 350)

        rightLayout = QVBoxLayout(rightSide)
        rightLayout.setContentsMargins(5, 5, 5, 5)

        titleLabel = QLabel("RECORDS", self)
        titleLabel.setStyleSheet("font-size: 14px; font-weight: bold; margin: 10px")
        titleLabel.setAlignment(Qt.AlignCenter)
        rightLayout.addWidget(titleLabel)

        tableWidget = QTableWidget(self)
        tableWidget.setColumnCount(4)
        tableWidget.setHorizontalHeaderLabels(
            ["Image", "Date", "Result", "Conf.%"]
        )
        
        tableWidget.setColumnWidth(0, 60)
        tableWidget.setColumnWidth(1, 60)
        tableWidget.setColumnWidth(2, 60)
        tableWidget.setColumnWidth(3, 60)

        tableWidget.setStyleSheet("""
        QTableWidget::corner { background-color: white; }
        QScrollBar:vertical { width: 10px; } 
        QScrollBar:horizontal { height: 10px; background-color: black } 
        QScrollBar::sub-line, QScrollBar::add-line { width: 5px; height: 5px }
    """)

        tableWidget.cellClicked.connect(self.loadImageFromTable)

        self.loadCSVRecords(tableWidget)
    
        rightLayout.addWidget(tableWidget)

        hLayout.addLayout(leftSide)
        hLayout.addWidget(rightSide)
        self.mainLayout.addLayout(hLayout)

        self.recordsTable = tableWidget

    def loadCSVRecords(self, tableWidget):
        csvFile = "records.csv"

        if not os.path.exists(csvFile):
            return

        with open(csvFile, newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)

        tableWidget.setRowCount(len(rows))

        for eachRow, row in enumerate(rows):
            for eachCol in range(4):
                if eachCol < len(row):
                    cellInfo = row[eachCol]
                else:
                    cellInfo = row[eachCol]

                item = QTableWidgetItem(cellInfo)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item.setToolTip(cellInfo)
                tableWidget.setItem(eachRow, eachCol, item)

            imageFilename = row[0]
            tableWidget.item(eachRow, 0).setData(Qt.UserRole, imageFilename)

    def loadImageFromTable(self, row, column):
        if column == 0:
            item = self.recordsTable.item(row, column)
            if item:
                imagePath = item.data(Qt.UserRole)
                if os.path.exists(imagePath):
                    pixmap = QPixmap(imagePath)
                    self.imageLabel.setPixmap(pixmap.scaled(
                        int(self.imageLabel.width() * 0.9),
                        int(self.imageLabel.height() * 0.9),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    ))
                else:
                    self.imageLabel.setText("Image Not Found")
            else:
                self.imageLabel.setText("Invalid File Path")


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

class ImageDropBox(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setCursor(Qt.PointingHandCursor)

        self.setStyleSheet("background-color: white; border: 0px solid rgb(20, 80, 120); border-radius: 40px")
        self.setMaximumSize(270, 270)
        self.setMinimumSize(270, 270)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.text = QLabel("Click or drag to upload image", self)
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setStyleSheet("color: gray;")
        layout.addWidget(self.text)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            if url.isLocalFile():
                filePath = url.toLocalFile()
                self.loadImage(filePath)
        event.acceptProposedAction()

    def mousePressEvent(self, event):
        filePath, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)"
        )

        if filePath:
            self.loadImage(filePath)

    def loadImage(self, filePath):
        pixmap = QPixmap(filePath)
        if pixmap.isNull():
            return

        if hasattr(self, "text"):
            self.layout().removeWidget(self.text)
            self.text.deleteLater()
            del self.text

        if hasattr(self, "imageLabel"):
            self.imageLabel.setPixmap(pixmap.scaled(int(self.width() * 0.9),
                        int(self.height() * 0.9), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.imageLabel = QLabel(self)
            self.imageLabel.setAlignment(Qt.AlignCenter)
            self.imageLabel.setPixmap(pixmap.scaled(int(self.width() * 0.9),
                        int(self.height() * 0.9), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.layout().addWidget(self.imageLabel)

    def showLoading(self):
        layout = self.layout()

        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        loadingLabel = QLabel("Running Classification...", self)
        loadingLabel.setAlignment(Qt.AlignCenter)
        loadingLabel.setStyleSheet("color: gray; font-size: 16px")
        layout.addWidget(loadingLabel)

    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = disclaimerWindow()
    window.show()
    sys.exit(app.exec_())