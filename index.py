from flask import Flask, jsonify, request;

from functions.getWorkers import getWorkers;
from functions.getWorkersByTitle import getWorkersByTitle;
from functions.getWorkersByOffice import getWorkersByOffice;
from functions.getWorkersByName import getWorkersByName;
from functions.getWorkersById import getWorkersById;

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

#PUT => edit a element by id
@app.route('/work/id/<int:id>', methods=["PUT"])
def editById(id):
    changedWorker = request.get_json()
    for indice, worker in enumerate(workers):
        if worker.get('id') == id:
            workers[indice].update(changedWorker);
            return jsonify(workers[indice]);
        

@app.route('/work/id/<int:id>', methods=["POST"])
def createWorker():
    
    
app.run(port=5000, host='localhost',debug=True);