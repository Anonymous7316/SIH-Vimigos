import mysql.connector      
con=mysql.connector.connect(host="localhost",user="root",passwd="root",database="vimigos")
rs=con.cursor()
def nametomail(n):
    rs.execute("select mail from info_1 where name='{}'".format(n,))
    data=rs.fetchall()
    for row in data:
        for c in row:
            print(c,end="\t")
        return c     
    con.close()                             
   

def mailtoname(m):
    rs.execute("select name from info_1 where mail='{}'".format(m,))
    data=rs.fetchall()
    for row in data:
        for c in row:
            print(c,end="\t")
        return c  
    con.close()                                    
    
"""mail=input("Enter the mail ")
mailtoname(mail)"""

