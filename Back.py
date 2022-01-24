import sqlite3
class Database:
    def __init__(self):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Book(Id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
        conn.commit()
        conn.close()

    def Insert(self,Title,Author,Year,ISBN):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(Title,Author,Year,ISBN))
        conn.commit()
        conn.close()

    def Search(self,Title="",Author="",Year="",isbn=""):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book WHERE Title=? OR Author=? OR Year=? OR ISBN=?",(Title,Author,Year,isbn))
        rows=cur.fetchall()
        conn.commit()
        conn.close()
        return rows

    def Update(self,id,Title,Author,year,isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("UPDATE book SET Title=?, Author=?, Year=?, ISBN=? WHERE Id=?",(Title,Author,year,isbn,id))
        conn.commit()
        conn.close()

    def Delete(self,id):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM book WHERE Id=?",(id,))
        conn.commit()
        conn.close()
    

    def View(self):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book")
        rows=cur.fetchall()
        conn.close()
        return rows
