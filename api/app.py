import mysql.connector
from flask import Flask, jsonify, request
from functions.GET import getWorkers;
from functions.PUT.editWorkerById import editById;
from functions.DELETE.deleteWorker import deleteWorker;
from functions.CREATE.createWorker import createWorker;

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Dudu1420!',
    database='dbwork',
    port='3306'
)

app = Flask(__name__)

@app.route('/work')
def get_all_workers(): return getWorkers.getWorkers(connection);

@app.route('/work/title/<title>', methods=["GET"])
def get_workers_by_title(title): 
    return getWorkers.getWorkersByTitle(title, connection);

@app.route('/work/office/<office>', methods=["GET"])
def get_workers_by_office(office):
    return getWorkers.getWorkersByOffice(office, connection);

@app.route('/work/name/<name>', methods=["GET"])
def get_workers_by_name(name):
    return getWorkers.getWorkersByName(name, connection);

@app.route('/work/id/<int:id>', methods=["GET"])
def get_workers_by_id(id):
    return getWorkers.getWorkersById(id, connection);

@app.route('/work/id/<int:id>', methods=["PUT"])
def edit_workers_by_id(id):
    return editById(id, connection);

@app.route('/work', methods=["POST"])
def create_worker():
    return createWorker(connection);

@app.route('/work/id/<int:id>', methods=["DELETE"])
def delete_workers(id):
    return deleteWorker(id, connection);

if __name__ == '__main__':
    app.run(port=5000, host='localhost',debug=True)
