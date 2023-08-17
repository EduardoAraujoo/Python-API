from flask import Flask, jsonify, request
from functions.errorFunc import errorFunc

def getWorkersByName(name, workers):
    self= "name";
    matchedWorkers = [worker for worker in workers if worker.get('name') == name]
    if not matchedWorkers:
        return errorFunc(self);
    return jsonify(matchedWorkers);