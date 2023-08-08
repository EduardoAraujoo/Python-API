import mysql.connector

conection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Dudu1420!',
    database='workerapi',
)

cursor = conection.cursor()

from flask import Flask, jsonify, request;

from functions.getWorkers import getWorkers;
from functions.getWorkersByTitle import getWorkersByTitle;
from functions.getWorkersByOffice import getWorkersByOffice;
from functions.getWorkersByName import getWorkersByName;
from functions.getWorkersById import getWorkersById;

from functions.editWorkerById import editById;
from functions.deleteWorker import deleteWorker;
from functions.createWorker import createWorker;

app = Flask(__name__)

workers = [
    {
        'id': 1,
        'name': 'Eduardo Araujo',
        'office': 'Desenvolvedor Fullstack',
        'title': 'Junior'
    },
    {
        'id': 2,
        'name': 'Eduardo Araujo',
        'office': 'Designer',
        'title': 'Senior'
    },
    {
        'id': 3,
        'name': 'Pedro Santos',
        'office': 'Desenvolvedor Back-End',
        'title': 'Pleno'
    },
    {
        'id': 4,
        'name': 'Mariana Costa',
        'office': 'Desenvolvedor Front-End',
        'title': 'Junior'
    }  
]

@app.route('/work')
def get_all_workers(): return getWorkers(workers);

@app.route('/work/title/<title>', methods=["GET"])
def get_workers_by_title(title): 
    return getWorkersByTitle(title, workers);

@app.route('/work/office/<office>', methods=["GET"])
def get_workers_by_office(office):
    return getWorkersByOffice(office, workers);

@app.route('/work/name/<name>', methods=["GET"])
def get_workers_by_name(name):
    return getWorkersByName(name, workers);

@app.route('/work/id/<int:id>', methods=["GET"])
def get_workers_by_id(id):
    return getWorkersById(id, workers);

@app.route('/work/id/<int:id>', methods=["PUT"])
def edit_workers_by_id(id):
    return editById(id, workers)

@app.route('/work', methods=["POST"])
def create_worker():
    return createWorker(workers);


@app.route('/work/id/<int:id>', methods=["DELETE"])
def delete_workers(id):
    return deleteWorker(id, workers);

    
    
app.run(port=5000, host='localhost',debug=True);
cursor.close()
conection.close()