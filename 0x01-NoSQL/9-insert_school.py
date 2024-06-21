#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def insert_school(mongo_collection, **kwargs):
    """ Insert a document in a collection based on kwargs """
    doc_id = mongo_collection.insert(kwargs)
    return doc_id
