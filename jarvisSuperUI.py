from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(979, 629)
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(-10, 0, 1451, 701))
        self.background.setStyleSheet("background-color:black;")
        self.background.setObjectName("background")

        



        self.ironManBackground = QtWidgets.QLabel(Form)
        self.ironManBackground.setGeometry(QtCore.QRect(740, 0, 241, 301))
        self.ironManBackground.setText("")
        self.ironManBackground.setPixmap(QtGui.QPixmap("./GUI files/Code_Template.gif"))
        self.ironManBackground.setScaledContents(True)
        self.ironManBackground.setObjectName("ironManBackground")


        self.jarvisGUI = QtWidgets.QLabel(Form)
        self.jarvisGUI.setGeometry(QtCore.QRect(-10, 10, 621, 391))
        self.jarvisGUI.setText("")
        self.jarvisGUI.setPixmap(QtGui.QPixmap("./GUI files/Siri.gif"))
        self.jarvisGUI.setScaledContents(True)
        self.jarvisGUI.setObjectName("jarvisGUI")


        self.startLabelNotButton = QtWidgets.QLabel(Form)
        self.startLabelNotButton.setGeometry(QtCore.QRect(560, 520, 211, 111))
        self.startLabelNotButton.setText("")
        self.startLabelNotButton.setPixmap(QtGui.QPixmap("./GUI files/Start.png"))
        self.startLabelNotButton.setScaledContents(True)
        self.startLabelNotButton.setObjectName("startLabelNotButton")


        self.quitLabelNotButton = QtWidgets.QLabel(Form)
        self.quitLabelNotButton.setGeometry(QtCore.QRect(770, 530, 211, 91))
        self.quitLabelNotButton.setText("")
        self.quitLabelNotButton.setPixmap(QtGui.QPixmap("./GUI files/Quit.png"))
        self.quitLabelNotButton.setScaledContents(True)
        self.quitLabelNotButton.setObjectName("quitLabelNotButton")


        self.timeLabel = QtWidgets.QLabel(Form)
        self.timeLabel.setGeometry(QtCore.QRect(10, 540, 241, 81))
        self.timeLabel.setText("")
        self.timeLabel.setPixmap(QtGui.QPixmap("./GUI files/gggf.jpg"))
        self.timeLabel.setScaledContents(True)
        self.timeLabel.setObjectName("timeLabel")


        self.dateLabel = QtWidgets.QLabel(Form)
        self.dateLabel.setGeometry(QtCore.QRect(10, 450, 241, 81))
        self.dateLabel.setText("")
        self.dateLabel.setPixmap(QtGui.QPixmap("./GUI files/gggf.jpg"))
        self.dateLabel.setScaledContents(True)
        self.dateLabel.setObjectName("dateLabel")


        self.ironManGIF = QtWidgets.QLabel(Form)
        self.ironManGIF.setGeometry(QtCore.QRect(540, 290, 411, 251))
        self.ironManGIF.setText("")
        self.ironManGIF.setPixmap(QtGui.QPixmap("./GUI files/Iron_Template_1.gif"))
        self.ironManGIF.setScaledContents(True)
        self.ironManGIF.setObjectName("ironManGIF")
        

        

        self.earthGIF = QtWidgets.QLabel(Form)
        self.earthGIF.setGeometry(QtCore.QRect(280, 420, 261, 191))
        self.earthGIF.setText("")
        self.earthGIF.setPixmap(QtGui.QPixmap("./GUI files/Ntuks.gif"))
        self.earthGIF.setScaledContents(True)
        self.earthGIF.setObjectName("earthGIF")

        self.dateTextBrowser = QtWidgets.QTextBrowser(Form)
        self.dateTextBrowser.setGeometry(QtCore.QRect(29, 470, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dateTextBrowser.setFont(font)
        self.dateTextBrowser.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:white;\n"
"border-radius:none;")
        self.dateTextBrowser.setObjectName("dateTextBrowser")
        self.timeTextBrowser = QtWidgets.QTextBrowser(Form)
        self.timeTextBrowser.setGeometry(QtCore.QRect(30, 561, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.timeTextBrowser.setFont(font)
        self.timeTextBrowser.setStyleSheet("background-color:transparent;\n"
"border:none;\n"
"color:white;\n"
"border-radius:none;")
        self.timeTextBrowser.setObjectName("timeTextBrowser")
        self.startPushButton = QtWidgets.QPushButton(Form)
        self.startPushButton.setGeometry(QtCore.QRect(574, 542, 181, 71))
        self.startPushButton.setStyleSheet("background-color:transparent;")
        self.startPushButton.setText("")
        self.startPushButton.setObjectName("startPushButton")
        self.quitPushButton = QtWidgets.QPushButton(Form)
        self.quitPushButton.setGeometry(QtCore.QRect(780, 540, 181, 71))
        self.quitPushButton.setStyleSheet("background-color:transparent;")
        self.quitPushButton.setText("")
        self.quitPushButton.setObjectName("quitPushButton")
        self.background.raise_()
        self.ironManBackground.raise_()
        self.jarvisGUI.raise_()
        self.startLabelNotButton.raise_()
        self.quitLabelNotButton.raise_()
        self.timeLabel.raise_()
        self.dateLabel.raise_()
        self.ironManGIF.raise_()
        self.earthGIF.raise_()
        self.timeTextBrowser.raise_()
        self.dateTextBrowser.raise_()
        self.startPushButton.raise_()
        self.quitPushButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.background.setText(_translate("Form", "TextLabel"))
        self.dateTextBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nirmala UI\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Date: 11-03-22</span></p></body></html>"))
        self.timeTextBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nirmala UI\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Time: 12:30:12</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
