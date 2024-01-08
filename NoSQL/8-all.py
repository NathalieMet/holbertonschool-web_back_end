#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection:

"""


def list_all(mongo_collection):
    """Write a Python function that lists all documents in a collection:"""
    all_documents = list(mongo_collection.find())
    return all_documents
