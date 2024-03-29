__Author__ = "Bill Lau"

from sqlalchemy import Table,MetaData,Column,Integer,String
from sqlalchemy.orm import mapper

metadata = MetaData()

user = Table('user',metadata,
             Column('id',Integer,primary_key=True),
             Column('name',String(50)),
             Column('fullname',String(50)),
             Column('Password',String(50)))

class User(object):
    def __init__(self,name,fullname,password):
        self.name = name
        self.fullname = fullname
        self.password = password

mapper(User,user)