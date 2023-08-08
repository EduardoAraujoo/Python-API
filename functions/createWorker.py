from flask import Flask, jsonify, request

def createWorker(workers):
    newWorker = request.get_json();
    workers.append(newWorker);
    
    return jsonify(workers);