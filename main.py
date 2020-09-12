import mysql.connector
from mysql.connector import Error

try: #connection är namnet på databasen för python
    connection = mysql.connector.connect(host='localhost',
                                         database='todo',
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
    question = input("would you like to enter another task?")
    if question == "yes":
        getValues()
    elif question != "yes":
        print("goodbye for now!")


    connection.commit()

def getValues():
    name = input("What's the name of the task?")
    category = input("what list do you want the task in? \n Lists: \n hemma \n skola \n jobb")
    timeEst = input("approximately how long will it take?")
    prio = input("how important is the task from 1-5?")
    todoInsert(name, category, timeEst, prio)

def openList():
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
smartPlan() 

def startUp():
    question = input("what would you like to do? \n to enter a task, type \"task\" "
                     "\n to look at your todo's in a list, type \"lists\" \n ")
    if question == "task":
        getValues()
    elif question != "hemma" or "skola" or "jobb":
        openList()

#startUp()

