import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employees(
        id integer primary key ,
        name TEXT,
        age text,
        doj text,
        email text,
        gender text,
        contect text,
        address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()



    def insert(self,name,age,doj,email,gender,contect,address):
        self.cur.execute('insert into employees values (null,?,?,?,?,?,?,?)',(name,age,doj,email,gender,contect,address))

        self.con.commit()

            #fetch all funtion
    def fetch(self):
        self.cur.execute('select * from employees')
        row=self.cur.fetchall()
        return row

    def remove(self,id):
        self.cur.execute('Delete from employees where id= ?',(id,))
        self.con.commit()

    def update(self,id,name,age,doj,email,gender,contect,address):
        self.cur.execute('update employees set name=?,age=?,doj=?,email=?,gender=?,contect=?,address=? where id=?',(name,age,doj,email,gender,contect,address,id))
        self.con.commit()



o =Database('employee.db')

o.fetch()

o.update('6','Zeen','20','01-12-1995','zeen@gmail.com','female','07527861','NO:20 Malpara Galle')