# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addTime.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogAddTime(object):
    def setupUi(self, DialogAddTime):
        DialogAddTime.setObjectName("DialogAddTime")
        DialogAddTime.resize(312, 373)
        DialogAddTime.setStatusTip("")
        DialogAddTime.setAccessibleDescription("")
        DialogAddTime.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.labelAddTime = QtWidgets.QLabel(DialogAddTime)
        self.labelAddTime.setGeometry(QtCore.QRect(20, 30, 121, 41))
        self.labelAddTime.setStyleSheet("border: none;\n"
"color: white;\n"
"font: 57 20pt \"Futura PT Demi\";")
        self.labelAddTime.setObjectName("labelAddTime")
        self.framePickTime = QtWidgets.QFrame(DialogAddTime)
        self.framePickTime.setGeometry(QtCore.QRect(20, 90, 270, 80))
        self.framePickTime.setStyleSheet("background-color: rgb(60, 60, 60);\n"
"border-radius: 15px;\n"
"border: 1px solid rgb(255, 255, 255);")
        self.framePickTime.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framePickTime.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framePickTime.setObjectName("framePickTime")
        self.labelH = QtWidgets.QLabel(self.framePickTime)
        self.labelH.setGeometry(QtCore.QRect(120, 26, 31, 31))
        self.labelH.setStyleSheet("border: none;\n"
"font: 57 22pt \"Futura PT Demi\";\n"
"color: white;")
        self.labelH.setAlignment(QtCore.Qt.AlignCenter)
        self.labelH.setObjectName("labelH")
        self.labelMIN = QtWidgets.QLabel(self.framePickTime)
        self.labelMIN.setGeometry(QtCore.QRect(200, 26, 61, 31))
        self.labelMIN.setStyleSheet("border: none;\n"
"font: 57 22pt \"Futura PT Demi\";\n"
"color: white;")
        self.labelMIN.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMIN.setObjectName("labelMIN")
        self.lineEditHours = QtWidgets.QLineEdit(self.framePickTime)
        self.lineEditHours.setGeometry(QtCore.QRect(80, 25, 41, 31))
        self.lineEditHours.setStyleSheet("border: none;\n"
"font: 57 22pt \"Futura PT Demi\";\n"
"color: white;border: none;")
        self.lineEditHours.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditHours.setObjectName("lineEditHours")
        self.lineEditMinutes = QtWidgets.QLineEdit(self.framePickTime)
        self.lineEditMinutes.setGeometry(QtCore.QRect(155, 25, 41, 31))
        self.lineEditMinutes.setStyleSheet("font: 57 22pt \"Futura PT Demi\";\n"
"color: white;\n"
"border: none;")
        self.lineEditMinutes.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMinutes.setObjectName("lineEditMinutes")
        self.iconClock = QtWidgets.QLabel(self.framePickTime)
        self.iconClock.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.iconClock.setStyleSheet("border: none;")
        self.iconClock.setText("")
        self.iconClock.setPixmap(QtGui.QPixmap(":/icons/schedule35.svg"))
        self.iconClock.setObjectName("iconClock")
        self.textEditOccupation = QtWidgets.QTextEdit(DialogAddTime)
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
        self.buttonADD = QtWidgets.QPushButton(DialogAddTime)
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

        self.retranslateUi(DialogAddTime)
        QtCore.QMetaObject.connectSlotsByName(DialogAddTime)

    def retranslateUi(self, DialogAddTime):
        _translate = QtCore.QCoreApplication.translate
        DialogAddTime.setWindowTitle(_translate("DialogAddTime", "Dialog"))
        self.labelAddTime.setText(_translate("DialogAddTime", "Add time:"))
        self.labelH.setText(_translate("DialogAddTime", "H"))
        self.labelMIN.setText(_translate("DialogAddTime", "MIN"))
        self.lineEditHours.setText(_translate("DialogAddTime", "0"))
        self.lineEditMinutes.setText(_translate("DialogAddTime", "0"))
        self.textEditOccupation.setHtml(_translate("DialogAddTime", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Futura PT Light\'; font-size:18pt; font-weight:24; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.buttonADD.setText(_translate("DialogAddTime", "ADD"))
# import add_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAddTime = QtWidgets.QDialog()
    ui = Ui_DialogAddTime()
    ui.setupUi(DialogAddTime)
    DialogAddTime.show()
    sys.exit(app.exec_())
