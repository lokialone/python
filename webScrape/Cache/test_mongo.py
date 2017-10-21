#!/usr/bin/env/python2.7
# use 

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test_database

if __name__ == "__main__":
    print db