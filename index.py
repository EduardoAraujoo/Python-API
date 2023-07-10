from flask import Flask, jsonify, request


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

#GET all workers
@app.route('/work')
def getWorkers():
    return jsonify(workers);

#GET worker by title
@app.route('/work/title/<title>', methods=["GET"])
def getWorkersByTitle(title):
    matchedWorkers = [worker for worker in workers if worker.get('title') == title]
    return jsonify(matchedWorkers);

#GET worker by office
@app.route('/work/office/<office>', methods=["GET"])
def getWorkersByOffice(office):
    matchedWorkers = [worker for worker in workers if worker.get('office') == office]
    return jsonify(matchedWorkers);
    return 'Certifique-se de que digitou o correto e utilizou da rota "/work/name/<name>"'

#GET worker by name
@app.route('/work/name/<name>', methods=["GET"])
def getWorkersByName(name):
    matchedWorkers = [worker for worker in workers if worker.get('name') == name]
    return jsonify(matchedWorkers);
    return 'Certifique-se de que digitou o Nome correto e utilizou da rota "/work/name/<name>"'

#GET worker by id
@app.route('/work/id/<int:id>', methods=["GET"])
def getWorkersById(id):
    for worker in workers:
        if worker.get('id') == id:
           return jsonify(worker);

# #PUT => edit a element by id
# @app.route('/work/<int:id>', methods=["PUT"])
# def editById(id):
#     changedWorker = request.get_json()
#     for indice, worker in enumerate(workers):
#         if worker.get('id') == id:
#             workers[indice].update(changedWorker);


app.run(port=5000, host='localhost',debug=True);