# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addTimeByTimer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogAddByTimer(object):
    def setupUi(self, DialogAddByTimer):
        DialogAddByTimer.setObjectName("DialogAddByTimer")
        DialogAddByTimer.resize(312, 373)
        DialogAddByTimer.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.frameTimeInfo = QtWidgets.QFrame(DialogAddByTimer)
        self.frameTimeInfo.setGeometry(QtCore.QRect(20, 90, 270, 80))
        self.frameTimeInfo.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"border-radius: 15px;\n"
"border: 1px solid rgb(255, 255, 255);")
        self.frameTimeInfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTimeInfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTimeInfo.setObjectName("frameTimeInfo")
        self.labelH = QtWidgets.QLabel(self.frameTimeInfo)
        self.labelH.setGeometry(QtCore.QRect(120, 26, 31, 31))
        self.labelH.setStyleSheet("border: none;\n"
"font: 57 22pt \"Futura PT Demi\";\n"
"color: white;")
        self.labelH.setAlignment(QtCore.Qt.AlignCenter)
        self.labelH.setObjectName("labelH")
        self.labelMIN = QtWidgets.QLabel(self.frameTimeInfo)
        self.labelMIN.setGeometry(QtCore.QRect(200, 26, 61, 31))
        self.labelMIN.setStyleSheet("border: none;\n"
"font: 57 22pt \"Futura PT Demi\";\n"
"color: white;")
        self.labelMIN.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMIN.setObjectName("labelMIN")
        self.iconClock = QtWidgets.QLabel(self.frameTimeInfo)
        self.iconClock.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.iconClock.setStyleSheet("border: none;")
        self.iconClock.setText("")
        self.iconClock.setPixmap(QtGui.QPixmap(":/icons/schedule35.svg"))
        self.iconClock.setObjectName("iconClock")
        self.timeHours = QtWidgets.QLabel(self.frameTimeInfo)
        self.timeHours.setGeometry(QtCore.QRect(80, 26, 41, 31))
        self.timeHours.setStyleSheet("border: none;\n"
"font: 57 22pt \"Futura PT Demi\";\n"
"color: white;")
        self.timeHours.setAlignment(QtCore.Qt.AlignCenter)
        self.timeHours.setObjectName("timeHours")
        self.timeMinutes = QtWidgets.QLabel(self.frameTimeInfo)
        self.timeMinutes.setGeometry(QtCore.QRect(155, 26, 41, 31))
        self.timeMinutes.setStyleSheet("border: none;\n"
"font: 57 22pt \"Futura PT Demi\";\n"
"color: white;")
        self.timeMinutes.setAlignment(QtCore.Qt.AlignCenter)
        self.timeMinutes.setObjectName("timeMinutes")
        self.labelAddTime = QtWidgets.QLabel(DialogAddByTimer)
        self.labelAddTime.setGeometry(QtCore.QRect(20, 30, 171, 41))
        self.labelAddTime.setStyleSheet("border: none;\n"
"color: white;\n"
"font: 57 20pt \"Futura PT Demi\";")
        self.labelAddTime.setObjectName("labelAddTime")
        self.textEditOccupation = QtWidgets.QTextEdit(DialogAddByTimer)
        self.textEditOccupation.setGeometry(QtCore.QRect(20, 190, 270, 61))
        self.textEditOccupation.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.textEditOccupation.setStatusTip("")
        self.textEditOccupation.setWhatsThis("")
        self.textEditOccupation.setAccessibleName("")
        self.textEditOccupation.setAccessibleDescription("")
        self.textEditOccupation.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"border-radius: 15px;\n"
"border: 1px solid rgb(255, 255, 255);\n"
"font: 25 18pt \"Futura PT Light\";\n"
"color: white;")
        self.textEditOccupation.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textEditOccupation.setDocumentTitle("")
        self.textEditOccupation.setPlaceholderText("")
        self.textEditOccupation.setObjectName("textEditOccupation")
        self.buttonADD = QtWidgets.QPushButton(DialogAddByTimer)
        self.buttonADD.setGeometry(QtCore.QRect(20, 300, 270, 51))
        self.buttonADD.setStyleSheet("QPushButton {\n"
"border: 1px solid rgb(255, 255, 255);\n"
"background-color: rgb(70, 70, 70);\n"
"border-radius: 15px;\n"
"font: 57 12pt \"Futura PT Demi\";\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 1px solid rgb(255, 255, 255);\n"
"background-color: rgb(90, 90, 90);\n"
"border-radius: 15px;\n"
"font: 57 12pt \"Futura PT Demi\";\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border: 2px solid rgb(255, 255, 255);\n"
"background-color: rgb(90, 90, 90);\n"
"border-radius: 15px;\n"
"font: 57 12pt \"Futura PT Demi\";\n"
"color: white;\n"
"}")
        self.buttonADD.setObjectName("buttonADD")

        self.retranslateUi(DialogAddByTimer)
        QtCore.QMetaObject.connectSlotsByName(DialogAddByTimer)

    def retranslateUi(self, DialogAddByTimer):
        _translate = QtCore.QCoreApplication.translate
        DialogAddByTimer.setWindowTitle(_translate("DialogAddByTimer", "Dialog"))
        self.labelH.setText(_translate("DialogAddByTimer", "H"))
        self.labelMIN.setText(_translate("DialogAddByTimer", "MIN"))
        self.timeHours.setText(_translate("DialogAddByTimer", "0"))
        self.timeMinutes.setText(_translate("DialogAddByTimer", "0"))
        self.labelAddTime.setText(_translate("DialogAddByTimer", "Timer adding:"))
        self.textEditOccupation.setHtml(_translate("DialogAddByTimer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Futura PT Light\'; font-size:18pt; font-weight:24; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.buttonADD.setText(_translate("DialogAddByTimer", "ADD"))
# import add_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAddByTimer = QtWidgets.QDialog()
    ui = Ui_DialogAddByTimer()
    ui.setupUi(DialogAddByTimer)
    DialogAddByTimer.show()
    sys.exit(app.exec_())
