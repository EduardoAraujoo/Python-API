from flask import Flask, jsonify, request

def getWorkersById(id, workers):
    for worker in workers:
        if worker.get('id') == id:
           return jsonify(worker);
    return jsonify["Not found. Have sure that you typed the correct id"];