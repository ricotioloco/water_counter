# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generator_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Generator(object):
    def setupUi(self, Generator):
        Generator.setObjectName("Generator")
        Generator.resize(574, 585)
        self.centralwidget = QtWidgets.QWidget(Generator)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 221, 71))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 120, 221, 71))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 200, 221, 101))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setText('0.15')
        self.textEdit_3.setToolTip('поле коэффициента\nчем больше значение\nтем больше разброс\nзначений\n0.15 по-умолчанию')
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(280, 40, 256, 491))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 540, 521, 34))
        self.pushButton.setObjectName("pushButton")
        Generator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Generator)
        QtCore.QMetaObject.connectSlotsByName(Generator)

    def retranslateUi(self, Generator):
        _translate = QtCore.QCoreApplication.translate
        Generator.setWindowTitle(_translate("Generator", "MainWindow"))
        self.textEdit.setPlaceholderText(_translate("Generator", "Введите количество дней"))
        self.textEdit_2.setPlaceholderText(_translate("Generator", "Введите итоговые показания счетчика"))
        self.textBrowser.setPlaceholderText(_translate("Generator", "Результат"))

        self.pushButton.setText(_translate("Generator", "Сгенерировать значения"))
