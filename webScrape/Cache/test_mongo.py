#!/usr/bin/env/python2.7
# need start mongo!!

from pymongo import MongoClient
import datetime
import pprint

client = MongoClient('localhost', 27017)
db = client.test_database
# post = {"author": "Mike",
#          "text": "My first blog post!",
#          "tags": ["mongodb", "python", "pymongo"],
#          "date": datetime.datetime.utcnow()}
posts = db.posts
# post_id = posts.insert_one(post).inserted_id



if __name__ == "__main__":
    pprint.pprint(posts.find_one())