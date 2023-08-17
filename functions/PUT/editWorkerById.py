from flask import Flask, jsonify, request

def editById(id, workers):
    changedWorker = request.get_json()
    for indice, worker in enumerate(workers):
        if worker.get('id') == id:
            workers[indice].update(changedWorker);
            
            return jsonify(workers[indice]);