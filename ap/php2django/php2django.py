#!/usr/bin/python

import os
import re
import sys
import types

sys.path.insert(0, os.path.abspath('..'))
settingsPath = "ap.settings.local"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settingsPath)
from django.conf import settings

from accounts.models import User, Trainee, TrainingAssistant

if __name__== "__main__":
    print User.objects.all()


class importUser:
    model=User
    query='SELECT * FROM user'
    
    class mapping:
        ID=0
        firstName=5
        nickName=8
        lastName=6
        middleName=7
        maidenName=9
        birthDate=11
        gender=10
        active=13
        def functionTest(self):
            return "function"

ignore = re.compile('^__.*__$')

for prop in importUser.mapping.__dict__:
    if not ignore.match(prop):
        var = importUser.mapping.__dict__[prop]
        if isinstance(var,types.FunctionType):
            print prop, var(importUser.mapping)
        else:
            print prop, var 

'''

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


'''