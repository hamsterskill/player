# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\player_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnfolderopen = QtWidgets.QPushButton(self.tab)
        self.btnfolderopen.setEnabled(True)
        self.btnfolderopen.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));\n"
"background-color: rgb(255, 255, 255);")
        self.btnfolderopen.setObjectName("btnfolderopen")
        self.gridLayout_3.addWidget(self.btnfolderopen, 0, 0, 1, 1)
        self.btnshuffle = QtWidgets.QPushButton(self.tab)
        self.btnshuffle.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));\n"
"background-color: rgb(255, 255, 255);")
        self.btnshuffle.setDefault(False)
        self.btnshuffle.setFlat(False)
        self.btnshuffle.setObjectName("btnshuffle")
        self.gridLayout_3.addWidget(self.btnshuffle, 0, 1, 1, 1)
        self.linefolder = QtWidgets.QLineEdit(self.tab)
        self.linefolder.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.linefolder.setReadOnly(True)
        self.linefolder.setObjectName("linefolder")
        self.gridLayout_3.addWidget(self.linefolder, 1, 0, 1, 2)
        self.tablefolder = QtWidgets.QTableWidget(self.tab)
        self.tablefolder.setObjectName("tablefolder")
        self.tablefolder.setColumnCount(2)
        self.tablefolder.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablefolder.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablefolder.setHorizontalHeaderItem(1, item)
        self.tablefolder.horizontalHeader().setVisible(True)
        self.tablefolder.horizontalHeader().setCascadingSectionResizes(False)
        self.tablefolder.horizontalHeader().setDefaultSectionSize(500)
        self.tablefolder.horizontalHeader().setHighlightSections(False)
        self.tablefolder.horizontalHeader().setSortIndicatorShown(False)
        self.tablefolder.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.tablefolder, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnplayandstop = QtWidgets.QPushButton(self.tab_2)
        self.btnplayandstop.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));\n"
"background-color: rgb(255, 255, 255);")
        self.btnplayandstop.setObjectName("btnplayandstop")
        self.gridLayout_2.addWidget(self.btnplayandstop, 4, 1, 1, 1)
        self.btnnew = QtWidgets.QPushButton(self.tab_2)
        self.btnnew.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));\n"
"background-color: rgb(255, 255, 255);")
        self.btnnew.setObjectName("btnnew")
        self.gridLayout_2.addWidget(self.btnnew, 4, 2, 1, 1)
        self.timeSlider = QtWidgets.QSlider(self.tab_2)
        self.timeSlider.setObjectName(u"horizontalSlider")
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setPageStep(1)
        self.gridLayout_2.addWidget(self.timeSlider, 3, 0, 1, 3)

        self.linenowplay = QtWidgets.QLineEdit(self.tab_2)
        self.linenowplay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.linenowplay.setReadOnly(True)
        self.linenowplay.setObjectName("linenowplay")
        self.gridLayout_2.addWidget(self.linenowplay, 0, 0, 1, 3)
        self.btnprewious = QtWidgets.QPushButton(self.tab_2)
        self.btnprewious.setAutoFillBackground(False)
        self.btnprewious.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));\n"
"background-color: rgb(255, 255, 255);")
        self.btnprewious.setObjectName("btnprewious")
        self.gridLayout_2.addWidget(self.btnprewious, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setStyleSheet("background-image: url(C:/Users/Admin/Desktop/Прога/прога/day_10/background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btnnew, self.btnplayandstop)
        MainWindow.setTabOrder(self.btnplayandstop, self.btnprewious)
        MainWindow.setTabOrder(self.btnprewious, self.linefolder)
        MainWindow.setTabOrder(self.linefolder, self.tablefolder)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Player"))
        self.btnfolderopen.setText(_translate("MainWindow", "Выбрать папку"))
        self.btnshuffle.setText(_translate("MainWindow", "Перемешать"))
        item = self.tablefolder.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tablefolder.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Длительность"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Список воспроизведения"))
        self.btnplayandstop.setText(_translate("MainWindow", "Play/Stop"))
        self.btnnew.setText(_translate("MainWindow", "Вперёд"))
        self.btnprewious.setText(_translate("MainWindow", "Назад"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Сейчас играет"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())