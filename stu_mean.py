import sqlite3

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

command = "CREATE TABLE peeps_avg (id INTEGER, avg INTEGER);"
c.execute(command)

for num in range(1,11):
    
    command = "SELECT mark FROM courses WHERE id = %s;"%num
    c.execute(command)
    studentavg = 0
    list1 = c.fetchall()
    leng = len(list1)
    for each in list1:
        studentavg += each[0]

    command = "INSERT INTO peeps_avg VALUES (%s,%s);"%(num,studentavg/leng)
    c.execute(command)

c.execute("SELECT * FROM peeps_avg;")
print c.fetchall()
#    print studentavg/ leng
#    print c.fetchall()[0][0]



db.commit() #save changes
db.close()  #close database
