# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 13:06:05 2021

@author: marco
"""

#R
def insert_reservation(command):
        n_guest=command[1]
        phone=command[2]
        name=command[3]
        conn=psycopg2.connect(dbname="cavallari_project_db",user="marco_cavallari",password="prog1",host="localhost")
        cur=conn.cursor()
        cur.execute("select * from progetto.table_reservation where name is null and max_capacity>=(select min(max_capacity) from progetto.table_reservation where max_capacity>=%s) limit 1;", ([n_guest]))
        tuple=cur.fetchall()
        cur3=conn.cursor()
        cur3.execute("select * from progetto.table_reservation where name=%s or phone=%s ;", (name,phone))
        unique_name=cur3.fetchall()
        if len(tuple)==1 and len(unique_name)==0:
            cur2=conn.cursor()
            cur2.execute("UPDATE progetto.table_reservation SET name=%s, phone = %s, n_guests= %s WHERE table_number=%s and max_capacity>=%s;", (name,phone,n_guest,tuple[0][0],n_guest))
            conn.commit()
            cur2.close()
        else:
            print("Error")
        cur.close()
        conn.close()

#U
def unreserved_tables():
    i=1
    conn=psycopg2.connect(dbname="cavallari_project_db",user="marco_cavallari",password="prog1",host="localhost")
    cur=conn.cursor()
    cur.execute("select * from progetto.table_reservation where name is null order by max_capacity;")
    tuple=cur.fetchall()
    for x in tuple:
        print(x[0],x[4])
        i=i+1

#S
def show_reservation_info(command):
    index_of_search=command[1]
    conn=psycopg2.connect(dbname="cavallari_project_db",user="marco_cavallari",password="prog1",host="localhost")
    cur=conn.cursor()
    cur.execute("select * from progetto.table_reservation where name=%s or phone=%s;",(index_of_search,index_of_search))
    tuple=cur.fetchall()
    if len(tuple)==0:
        print("Error")
    for x in tuple:
         print(x[0],x[3],x[4],x[2],x[1])

#C
def cancel_reservation(command):
    index_of_search=command[1]
    conn=psycopg2.connect(dbname="cavallari_project_db",user="marco_cavallari",password="prog1",host="localhost")
    cur=conn.cursor()
    cur.execute("update progetto.table_reservation set name=null,phone=null,n_guests=0 where name=%s or phone=%s;",(index_of_search,index_of_search))
    if cur.rowcount==0:
        print("Error")
    conn.commit()


#L
def list_reservation():
    conn=psycopg2.connect(dbname="cavallari_project_db",user="marco_cavallari",password="prog1",host="localhost")
    cur=conn.cursor()
    cur.execute("select * from progetto.table_reservation where name is not null;")
    tuple=cur.fetchall()
    for x in tuple:
         print(x[0],x[3],x[4],x[2],x[1])


#NT
def number_reserved():
    conn=psycopg2.connect(dbname="cavallari_project_db",user="marco_cavallari",password="prog1",host="localhost")
    cur=conn.cursor()
    cur.execute("select count(*) from progetto.table_reservation where name is not null;")
    tuple=cur.fetchall()
    print(tuple[0][0])


#NT g
def number_reserved_guest(command):
    n=command[1]
    conn=psycopg2.connect(dbname="cavallari_project_db",user="marco_cavallari",password="prog1",host="localhost")
    cur=conn.cursor()
    cur.execute("select count(*) from progetto.table_reservation where n_guests=%s;",[n])
    tuple=cur.fetchall()
    print(tuple[0][0])


#NG
def count_guest():
    conn=psycopg2.connect(dbname="cavallari_project_db",user="marco_cavallari",password="prog1",host="localhost")
    cur=conn.cursor()
    cur.execute("select sum(n_guests) from progetto.table_reservation;")
    tuple=cur.fetchall()
    print(tuple[0][0])


#NU
def unreserved_seats():
    unreserved_seats=0
    conn=psycopg2.connect(dbname="cavallari_project_db",user="marco_cavallari",password="prog1",host="localhost")
    cur=conn.cursor()
    cur.execute("select sum(max_capacity-n_guests) from progetto.table_reservation;")
    tuple=cur.fetchall()
    unreserved_seats=tuple[0][0]
    cur2=conn.cursor()
    cur2.execute("select sum(max_capacity) from progetto.table_reservation where name is null;")
    tuple2=cur2.fetchall()
    unreserved_seats=unreserved_seats+tuple2[0][0]
    print(unreserved_seats)


#GU
def show_tables():
    conn=psycopg2.connect(dbname="cavallari_project_db",user="marco_cavallari",password="prog1",host="localhost")
    cur=conn.cursor()
    cur.execute("select table_number,n_guests,max_capacity from progetto.table_reservation order by max_capacity-n_guests desc;")
    tuple=cur.fetchall()
    for x in tuple:
        print(x[0],x[1],x[2])


#GR
def show_unreserved_tables():
    conn=psycopg2.connect(dbname="cavallari_project_db",user="marco_cavallari",password="prog1",host="localhost")
    cur=conn.cursor()
    cur.execute("select table_number,n_guests,max_capacity from progetto.table_reservation where name is not null order by max_capacity-n_guests desc;")
    tuple=cur.fetchall()
    for x in tuple:
        print(x[0],x[1],x[2])


def main():
    command=['start']
    while command[0]!='E':
        command=list(map(str,input('>').split()))
        if command[0]=='R' and len(command)==4:
            insert_reservation(command)
        elif command[0]=='U' and len(command)==1:
            unreserved_tables()
        elif command[0]=='S' and len(command)==2:
            show_reservation_info(command)
        elif command[0]=='C' and len(command)==2:
            cancel_reservation(command)
        elif command[0]=='L' and len(command)==1:
            list_reservation()
        elif command[0]=='NT' and len(command)==1:
            number_reserved()
        elif command[0]=='NT' and len(command)==2:
            number_reserved_guest(command)
        elif command[0]=='NG' and len(command)==1:
            count_guest()
        elif command[0]=='NU' and len(command)==1:
            unreserved_seats()
        elif command[0]=='GU' and len(command)==1:
            show_tables()
        elif command[0]=='GR' and len(command)==1:
            show_unreserved_tables()


import psycopg2
main()
