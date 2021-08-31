from PyQt5 import QtCore, QtGui, QtWidgets

import main


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 303)
        MainWindow.setMouseTracking(False)
        MainWindow.setWindowTitle("AutomatedResultsBot")
        MainWindow.setStyleSheet("color: rgb(0, 255, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 200, 75, 23))

        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("""
                                    QPushButton
                                    {
                                    
                                    transition: all .5s ease;
    color:#e7eeef;
    border: 3px solid white;
    font-family:'Montserrat', sans-serif;
    text-transform: uppercase;
    text-align: center;
    line-height: 1;
    font-size: 12px;
    font-weight:bold;
    background-color : #1ba94c;
    padding: 1px;
    outline: none;
    
    border-radius: 2px;
    border-color:#FFFFFF;
                                    }
                                    QPushButton::hover
                                    {
                                    color: #1ba94c;
    background-color: #e7eeef;
    font-weight:bold;
    border-radius:1px;
    border-color: #1ba94c;
                                    }
                                    QPushButton::focus
                                    {
                                    box-shadow: 0 0.5em 0.5em -0.4em var(--hover);
                                    transform: translateY(-0.25em);
                                    }
            """
                                      )
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 110, 91, 22))
        self.comboBox.setStyleSheet("bg-color:red;\n"
                                    "color:#1ba94c ;\n"
                                    "shadow:5px;\n"
                                    "\n"
                                    "")

        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setStyleSheet("QComboBox{color: rgb(255, 255, 255 );\n"
                                    "background-color: #1ba94c;\n"
                                    "background-image:url(background.png);}\n"
                                    "text-align:center;}\n"
                                    "QComboBox QAbstractItemView{border: 0px;color:black}")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 110, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setStyleSheet("QComboBox{color: rgb(255, 255, 255 );\n"
                                      "background-color: #1ba94c;\n"
                                      "background-image:url(background.png);}\n"
                                      "QComboBox QAbstractItemView{border: 0px;color:black}")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(290, 110, 81, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")

        self.comboBox_3.setStyleSheet("QComboBox{color: rgb(255, 255, 255 );\n"
                                      "background-color: #1ba94c;\n"
                                      "background-image:url(background.png);}\n"
                                      "QComboBox QAbstractItemView{border: 0px;color:#000000}")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(400, 110, 81, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setStyleSheet("QComboBox{color: rgb(255, 255, 255 );\n"
                                      "background-color: #1ba94c;\n"
                                      "background-image:url(background.png);}\n"
                                      "QComboBox QAbstractItemView{border: 0px;color:#000000}")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 541, 41))
        self.label.setStyleSheet("background-color: #1ba94c  ;\n"
                                 "color:#ffffff;\n"
                                 "font-align:center;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 221, 20))
        self.label_2.setStyleSheet("color:#FFFFFF;")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.comboBox.setItemText(0, _translate("MainWindow", "CIV"))
        self.comboBox.setItemText(1, _translate("MainWindow", "CSE"))
        self.comboBox.setItemText(2, _translate("MainWindow", "EEE"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ECE"))
        self.comboBox.setItemText(4, _translate("MainWindow", "MEC"))
        self.comboBox.setItemText(5, _translate("MainWindow", "IT"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1 YEAR"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2 YEAR"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3 YEAR"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4 YEAR"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1 SEM"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2 SEM"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "C"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Automated Results Bot</span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>"))
        self.pushButton.clicked.connect(self.call)

    def call(self):
        branch = self.comboBox.currentText()
        year = self.comboBox_2.currentText()
        sem = self.comboBox_3.currentText()
        section = self.comboBox_4.currentText()
        code = year[0] + '_' + branch + '-' + section               # 2_CIV-A
        filename = year + '_' + branch + '_' + sem + '-' + section  # eg: 2Year_CIV_1SEM-A
        # print(filename)
        main.find_sub(code)
        main.collect(code, filename)

        print("Execution Completed")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
