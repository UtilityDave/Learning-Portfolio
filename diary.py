#!/usr/bin/env python3

from peewee import *
import datetime

db = SqliteDatabase('diary.db')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now())
  
    class Meta:
        database = db

def initialize():
    """
    Create the database and the table if they don't exist.
    """
    db.connect()
    db.create_tables([Entry], safe = True)  
    
def menu_loop():
  """
  Show Me The Menu
  """
  
def add_entry():
  """
  Adds an entry
  """  
  
def view_entries():
  """
  Displays entries
  """
  
def delete_entry(entry):
  """
  Deletes entry passed in as argument
  """
  
if __name__ == '__main__':
  initialize()
  menu_loop()
  
