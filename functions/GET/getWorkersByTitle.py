from flask import Flask, jsonify, request
from functions.errorFunc import errorFunc
# from functions.mysqlFunctions.cursor import cursor_get;

def getWorkersByTitle(title, connection, my_workers):
    
    # cursor_get(connection)
    
    self = "title";
    matchedWorkers = [worker for worker in my_workers if worker.get('title') == title]
    if not matchedWorkers:
        return errorFunc(self);
    return jsonify(matchedWorkers);