#!/usr/bin/python
import MySQLdb
import pickle

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="lifeunion", # your password
                      db="phptodjangodb") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM user ")

num_fields = len(cur.description)
field_names = [i[0] for i in cur.description]

f=open('phpdata','w')
g=open('userdictionary', 'w')

for aName in field_names :
    f.write(' '.join(str(anID) for anID in aName) + '\n')

length = 0
inclusive = cur.fetchall()

for row in inclusive :
    length+=1;
    f.write(' '.join(str(onetuple) for onetuple in row) + '\n')

keys = field_names
values = []
madeList = []
overallList = []
dummyDict = []

for n in range(0,length-1):
    
    for indexKey in range(0,num_fields-1):
        values.append(inclusive[n][indexKey])
    
    dummyDict = dict(zip(keys,values))
    madeList.append(dummyDict)
    overallList.append(madeList)
    values = []
    madeList =[]

output = open('userphp.pickle','wb')
pickle.dump(overallList, output)
output.close()

reading = open('userphp.pickle', 'rb')
userinfo = pickle.load(reading)
print userinfo

g.write(' '.join(str(atuple) for atuple in userinfo) + '\n')


