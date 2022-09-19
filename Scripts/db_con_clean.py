"""Clean old DB"""

from distutils.command.config import config
from typing_extensions import Self
from numpy import extract
import py
import requests
import pandas as pd
import os
import sqlite3
import datetime
import time

initialdate = []
finaldate = []
portaltp_executivo=[]
metlist = []
local_apilist = []
local_db = []
exec(open("scripts/API_organization.py").read())
exec(open("config.py").read())

def dbclean():
    """Cleaning old DB"""

    os.remove("C:\TempData\Julius.db") if os.path.exists("C:\TempData\Julius.db") else None
    return print('Database Cleaned!')

def dbstart():
    """Start connection and cursor setup"""

    conn = sqlite3.connect('C:\TempData\Julius.db')
    type(conn)
    cur = conn.cursor()
    type(cur)
    print('Conection to Database Created')
    return conn

def dbclose(conn):
    """Close connection"""

    conn.close()

    return print('Database Closed')

dbclean()