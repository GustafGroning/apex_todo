from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 300, 300)
    #sätter 4 parametrar, xpos, ypos, width, height för rutan.
    win.setWindowTitle("Apex Todo")

    label = QtWidgets.QLabel(win)
    label.setText("My first label")
    label.move(50,50)
    win.show()
    sys.exit(app.exec_())





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(489, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.smartPlanButton = QtWidgets.QPushButton(self.centralwidget)
        self.smartPlanButton.setGeometry(QtCore.QRect(130, 170, 231, 141))
        self.smartPlanButton.setObjectName("smartPlanButton")
        self.addTaskButton = QtWidgets.QPushButton(self.centralwidget)
        self.addTaskButton.setGeometry(QtCore.QRect(160, 80, 171, 61))
        self.addTaskButton.setObjectName("addTaskButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 350, 161, 111))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 350, 161, 111))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.smartPlanButton.setText(_translate("MainWindow", "SMART PLAN"))
        self.addTaskButton.setText(_translate("MainWindow", "Add Task"))
        self.pushButton_2.setText(_translate("MainWindow", "Statistics"))
        self.pushButton_3.setText(_translate("MainWindow", "Lists"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
 
Ui_MainWindow()