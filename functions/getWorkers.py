from flask import Flask, jsonify, request

def getWorkers(workers):
    return jsonify(workers);