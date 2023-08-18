import mysql.connector
from flask import Flask, jsonify, request;


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Dudu1420!',
    database='dbwork',
    port='3306'
)



from functions.GET.getWorkers import getWorkers;
from functions.GET.getWorkersByTitle import getWorkersByTitle;
from functions.GET.getWorkersByOffice import getWorkersByOffice;
from functions.GET.getWorkersByName import getWorkersByName;
from functions.GET.getWorkersById import getWorkersById;

from functions.PUT.editWorkerById import editById;
from functions.DELETE.deleteWorker import deleteWorker;
from functions.CREATE.createWorker import createWorker;

app = Flask(__name__)

@app.route('/work')
def get_all_workers(): return getWorkers(connection);

@app.route('/work/title/<title>', methods=["GET"])
def get_workers_by_title(title): 
    return getWorkersByTitle(title, connection);

# @app.route('/work/office/<office>', methods=["GET"])
# def get_workers_by_office(office):
#     return getWorkersByOffice(office, workers);

# @app.route('/work/name/<name>', methods=["GET"])
# def get_workers_by_name(name):
#     return getWorkersByName(name, workers);

# @app.route('/work/id/<int:id>', methods=["GET"])
# def get_workers_by_id(id):
#     return getWorkersById(id, workers);

@app.route('/work/id/<int:id>', methods=["PUT"])
def edit_workers_by_id(id):
    return editById(id, connection);

@app.route('/work', methods=["POST"])
def create_worker():
    return createWorker(connection);

@app.route('/work/id/<int:id>', methods=["DELETE"])
def delete_workers():
    return deleteWorker(connection);

app.run(port=5000, host='localhost',debug=True)
