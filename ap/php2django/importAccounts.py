#!/usr/bin/python

import os
import sys

if __name__== "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from php2django import php2django

from accounts.models import User, Trainee, TrainingAssistant

class importUser(php2django.importTemplate):
    model=User
    query='SELECT * FROM user'
    key=0
    
    class mapping:
        firstname=5
        nickname=8
        lastname=6
        middlename=7
        maidenname=9
        date_of_birth=11
        gender=10
        is_active=13
#         def functionTest(self,queryResult):
#             return str(queryResult)

if __name__== "__main__":
    temp = importUser()
    temp.doImport()