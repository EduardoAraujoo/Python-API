from flask import Flask, jsonify, request
from functions.errorFunc import errorFunc


def getWorkersByTitle(title, workers):
    self = "title";
    matchedWorkers = [worker for worker in workers if worker.get('title') == title]
    if not matchedWorkers:
        return errorFunc(self);
    return jsonify(matchedWorkers);