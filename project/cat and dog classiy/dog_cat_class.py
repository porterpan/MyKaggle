# -*- coding: utf-8 -*-

"""
Module implementing cat_or_dog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from Ui_dog_cat_class import Ui_cat_or_dog

import os
from keras.models import load_model
import numpy as np
import cv2



class cat_or_dog(QDialog, Ui_cat_or_dog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(cat_or_dog, self).__init__(parent)
        self.setupUi(self)
        self.image_resize_target = 150
        self.model = load_model("cats_and_dogs_small_1.h5")


    def process_image(self, img):
        min_side = self.image_resize_target
        size = img.shape
        h, w = size[0], size[1]
        # 长边缩放为min_side
        scale = max(w, h) / float(min_side)
        new_w, new_h = int(w / scale), int(h / scale)
        resize_img = cv2.resize(img, (new_w, new_h))
        # 填充至min_side * min_side
        if new_w % 2 != 0 and new_h % 2 == 0:
            top, bottom, left, right = (min_side - new_h) / 2, (min_side - new_h) / 2, (min_side - new_w) / 2 + 1, (
                        min_side - new_w) / 2
        elif new_h % 2 != 0 and new_w % 2 == 0:
            top, bottom, left, right = (min_side - new_h) / 2 + 1, (min_side - new_h) / 2, (min_side - new_w) / 2, (
                        min_side - new_w) / 2
        elif new_h % 2 == 0 and new_w % 2 == 0:
            top, bottom, left, right = (min_side - new_h) / 2, (min_side - new_h) / 2, (min_side - new_w) / 2, (
                        min_side - new_w) / 2
        else:
            top, bottom, left, right = (min_side - new_h) / 2 + 1, (min_side - new_h) / 2, (min_side - new_w) / 2 + 1, (
                        min_side - new_w) / 2
        pad_img = cv2.copyMakeBorder(resize_img, int(top), int(bottom), int(left), int(right), cv2.BORDER_CONSTANT,
                                     value=[0, 0, 0])  # 从图像边界向上,下,左,右扩的像素数目

        return pad_img

    @pyqtSlot()
    def on_pushButton_clicked(self):

        self.label_result.setText("识别结果： ")

        images_1, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                         "Image Files(*.jpg *.png *.jpeg *.ico)")  # 设置文件扩展名过滤,注意用双分号间隔
        pixmap = QtGui.QPixmap(images_1)
        self.label_origin_image_dis.setPixmap(pixmap.scaled(150,150))

        input = cv2.imread(images_1)
        input = self.process_image(input)
        input = cv2.cvtColor(input, cv2.COLOR_BGR2RGB)
        pre_x = np.expand_dims(input, axis=0)
        pre_y = self.model.predict(pre_x)
        print(pre_y)
        print("预测结果输出：")
        if pre_y[0] > 0.5:
            print("识别结果：狗狗")
            self.label_result.setText("识别结果：狗狗")
        else:
            print("识别结果：猫猫")
            self.label_result.setText("识别结果：猫猫")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = cat_or_dog()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ui.setWindowIcon(icon)
    ui.show()
    sys.exit(app.exec_())