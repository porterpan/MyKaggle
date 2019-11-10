# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/porter/文档/github workspace/MyKaggle/project/cat and dog classiy/dog_cat_class.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cat_or_dog(object):
    def setupUi(self, cat_or_dog):
        cat_or_dog.setObjectName("cat_or_dog")
        cat_or_dog.resize(255, 293)
        cat_or_dog.setSizeGripEnabled(True)
        self.label_origin_image_dis = QtWidgets.QLabel(cat_or_dog)
        self.label_origin_image_dis.setGeometry(QtCore.QRect(40, 50, 150, 150))
        self.label_origin_image_dis.setAutoFillBackground(False)
        self.label_origin_image_dis.setText("")
        self.label_origin_image_dis.setObjectName("label_origin_image_dis")
        self.label_tips = QtWidgets.QLabel(cat_or_dog)
        self.label_tips.setGeometry(QtCore.QRect(50, 10, 141, 21))
        self.label_tips.setObjectName("label_tips")
        self.pushButton = QtWidgets.QPushButton(cat_or_dog)
        self.pushButton.setGeometry(QtCore.QRect(20, 230, 191, 27))
        self.pushButton.setObjectName("pushButton")
        self.label_result = QtWidgets.QLabel(cat_or_dog)
        self.label_result.setGeometry(QtCore.QRect(70, 260, 91, 31))
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")

        self.retranslateUi(cat_or_dog)
        QtCore.QMetaObject.connectSlotsByName(cat_or_dog)

    def retranslateUi(self, cat_or_dog):
        _translate = QtCore.QCoreApplication.translate
        cat_or_dog.setWindowTitle(_translate("cat_or_dog", "Dialog"))
        self.label_tips.setText(_translate("cat_or_dog", "原始图片加载显示"))
        self.pushButton.setText(_translate("cat_or_dog", "选择待识别的猫或狗图片"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cat_or_dog = QtWidgets.QDialog()
    ui = Ui_cat_or_dog()
    ui.setupUi(cat_or_dog)
    cat_or_dog.show()
    sys.exit(app.exec_())
