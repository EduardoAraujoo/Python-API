from flask import Flask, jsonify, request

def deleteWorker(id, workers):
    for indice, worker in enumerate(workers):
        if worker.get('id') == id:
            del workers[indice]
        
        return jsonify(workers)