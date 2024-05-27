#!/usr/bin/env python3
"""Write a Python script that provides some stats about Nginx logs stored
in MongoDB
"""


from pymongo import MongoClient

""" Connect to MongoDB """
client = MongoClient("mongodb://localhost:27017/")
"""Update with the MongoDB connection string"""
db = client.logs
collection = db.nginx


def get_logs_count():
    """Get the total number of logs."""
    return collection.count_documents({})


def get_method_stats():
    """Get the count of logs for each HTTP method."""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    stats = {method: collection.count_documents({"method": method})
             for method in methods}
    return stats


def get_status_endpoint_count():
    """Get the count of logs with method=GET and path=/status."""
    return collection.count_documents({"method": "GET", "path": "/status"})


def display_stats():
    """Display the requested statistics."""
    """Display total logs count"""
    total_logs = get_logs_count()
    print(f"{total_logs} logs")

    """Display method statistics"""
    method_stats = get_method_stats()
    print("Methods:")
    for method, count in method_stats.items():
        print(f"\tmethod {method}: {count}")

    """Display count of logs with method=GET and path=/status"""
    status_logs_count = get_status_endpoint_count()
    print(f"{status_logs_count} status check")


if __name__ == "__main__":
    display_stats()
