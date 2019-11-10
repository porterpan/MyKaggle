# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/porter/文档/github workspace/MyKaggle/project/RMBRecongition/GUI_Project/RMBRecognition.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RMBRecognition(object):
    def setupUi(self, RMBRecognition):
        RMBRecognition.setObjectName("RMBRecognition")
        RMBRecognition.resize(255, 293)
        RMBRecognition.setSizeGripEnabled(True)
        self.label_origin_image_dis = QtWidgets.QLabel(RMBRecognition)
        self.label_origin_image_dis.setGeometry(QtCore.QRect(10, 50, 240, 120))
        self.label_origin_image_dis.setAutoFillBackground(False)
        self.label_origin_image_dis.setText("")
        self.label_origin_image_dis.setObjectName("label_origin_image_dis")
        self.label_tips = QtWidgets.QLabel(RMBRecognition)
        self.label_tips.setGeometry(QtCore.QRect(50, 10, 141, 21))
        self.label_tips.setObjectName("label_tips")
        self.pushButton = QtWidgets.QPushButton(RMBRecognition)
        self.pushButton.setGeometry(QtCore.QRect(20, 230, 191, 27))
        self.pushButton.setObjectName("pushButton")
        self.label_result = QtWidgets.QLabel(RMBRecognition)
        self.label_result.setGeometry(QtCore.QRect(50, 260, 131, 31))
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")

        self.retranslateUi(RMBRecognition)
        QtCore.QMetaObject.connectSlotsByName(RMBRecognition)

    def retranslateUi(self, RMBRecognition):
        _translate = QtCore.QCoreApplication.translate
        RMBRecognition.setWindowTitle(_translate("RMBRecognition", "Dialog"))
        self.label_tips.setText(_translate("RMBRecognition", "原始图片加载显示"))
        self.pushButton.setText(_translate("RMBRecognition", "选择待识别的人民币面值"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RMBRecognition = QtWidgets.QDialog()
    ui = Ui_RMBRecognition()
    ui.setupUi(RMBRecognition)
    RMBRecognition.show()
    sys.exit(app.exec_())
