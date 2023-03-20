#Issue Module
import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os
def clrscreen():
 print('\n' *5)
def ShowIssuedBooks():
 try:
     os.system('cls')
     cnx = connection.MySQLConnection(user='root', password='root1234',host='localhost',database='Library')
     Cursor = cnx.cursor()
     query = ("SELECT B.bno,bname,M.mno,mname,d_o_issue,d_o_ret FROM bookRecord B,issue I"\
 ",member M where B.bno=I.bno and I.mno=M.mno")
     Cursor.execute(query)
     for (Bno,Bname,Mno,Mname,doi,dor) in Cursor:
         print("Book Code : ",Bno)
         print("Book Name : ",Bname)
         print("Member Code : ",Mno)
         print("Member Name : ",Mname)
         print("Date of issue : ",doi)
         print("Date of return : ",dor)
     Cursor.close()
     cnx.close()
     print("Success")
 except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
     else:
         print(err)
     cnx.close()

def issueBook():
 try:
     cnx = connection.MySQLConnection(user='root',password='root1234',host='127.0.0.1',database='Library')
     Cursor = cnx.cursor()
     bno=input("Enter Book Code to issue : ")
     mno=input("Enter Member Code : ")
     print("Enter Date of Issue (Date,Month and Year seperately): ")
     DD=int(input("Enter Date : "))
     MM=int(input("Enter Month : "))
     YY=int(input("Enter Year : "))

     Qry = ("INSERT INTO issue (bno,mno,d_o_issue)"\
"VALUES (%s, %s, %s)")
     data = (bno,mno,date(YY,MM,DD))
     Cursor.execute(Qry,data)
     cnx.commit()
     Cursor.close()
     cnx.close()
     print("Record Inserted")
 except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
     else:
         print(err)
     cnx.close()
     
def returnBook():
 try:
     cnx = connection.MySQLConnection(user='root',password='root1234',host='127.0.0.1',database='Library')
     Cursor = cnx.cursor()
     bno=input("Enter Book Code of Book to be returned to the Library : ")
     Mno=input("Enter Member Code of Member who is returning Book : ")
     retDate=date.today()
     Qry =("""Update Issue set d_o_ret= %s WHERE BNO = %s and Mno= %s """)
     rec=(retDate,bno,Mno)
     Cursor.execute(Qry,rec)

     cnx.commit()
     Cursor.close()
     cnx.close()
     print(Cursor.rowcount,"Book Returned Successfully")
 except mysql.connector.Error as err:
     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Something is wrong with your user name or password")
     elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database does not exist")
     else:
         print(err)
     cnx.close()




