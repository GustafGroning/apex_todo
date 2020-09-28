import mysql.connector
from mysql.connector import Error
from PyQt5 import QtCore, QtGui, QtWidgets


try: #connection är namnet på databasen för python
    connection = mysql.connector.connect(host='localhost',
                                         database='todo_db',
                                         user='root',
                                        password='gurkan')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        #print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)

# myCursor är det generella objektet för att interagera med DBn, t.ex myCursor.execute
myCursor = connection.cursor()



def todoInsert(name, category, timeEst, prio):
    sql = "insert into items (name, category, estimated_time, priority) values"
    todoIn = ("(\"%s\", \"%s\", %s, \"%s\");" % (name,category,timeEst, prio))
    insertQuery = (sql + todoIn)
    print(insertQuery)
    sql_query = str(insertQuery)
    myCursor.execute(sql_query)
    connection.commit()

    

def getValues(taskName, taskList, taskTime, taskPrio):
    print("running getValues")
    name = taskName
    category = taskList
    timeEst = taskTime
    prio = taskPrio
    todoInsert(name, category, timeEst, prio)

def openList():
    showLists = "select DISTINCT(category) from items;"
    myCursor.execute(showLists)
    myRes = myCursor.fetchall()
    for x in myRes:
        print(x)    
    listName = input("which list would you like to see? \n (hemma, skola eller jobb) \n")
    myCursor.execute("select * from items where category = \"%s\" " % (listName))
    myRes = myCursor.fetchall()
    for x in myRes:
        print(x)

def smartPlan():   #TODO fixa så att priority går på MAX, lista så många som finns
    category = input("which list can you work from?")
    time = input("how much time do you have?")
    smartQuery = "SELECT * from items WHERE category = \"%s\" AND priority = 5 AND estimated_time <= %s LIMIT 1" % (category, time) 
    #TODO: limit 1 med högsta estimated_time
    myCursor.execute(smartQuery)
    myRes = myCursor.fetchall()
    for x in myRes: 
        print(x)
#smartPlan() 


    









def startUp():
    question = input("what would you like to do? \n to enter a task, type \"task\" "
                     "\n to look at your todo's in a list, type \"lists\" \n ")
    if question == "task":
        getValues()
    elif question != "hemma" or "skola" or "jobb":
        openList()



#startUp()





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 450, 171, 81))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 130, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 270, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 200, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 340, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 130, 70, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 200, 60, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 270, 60, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 340, 91, 16))
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.getInput)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "Task name"))
        self.label_2.setText(_translate("MainWindow", "Task list"))
        self.label_3.setText(_translate("MainWindow", "priority"))
        self.label_4.setText(_translate("MainWindow", "time estimate"))

    def getInput(self):
        #kör en funktion som bara sparar variabler, skicka dem senare till funktionerna.
        taskName = self.lineEdit.text()
        print(taskName)
        taskList = self.lineEdit_3.text()
        print(taskList)
        taskPrio = self.lineEdit_2.text()
        print(taskPrio)
        taskTime = self.lineEdit_4.text()
        print(taskTime)
        getValues(taskName, taskList, taskTime, taskPrio)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())