from flask import Flask, jsonify, request
from functions.errorFunc import errorFunc

def getWorkersByOffice(office, workers):
    self = "office";
    matchedWorkers = [worker for worker in workers if worker.get('office') == office]
    if not matchedWorkers:
        return errorFunc(self);
    return jsonify(matchedWorkers);