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
    self = "title";
    matchedWorkers = [worker for worker in workers if worker.get('title') == title]
    if not matchedWorkers:
        return errorFunc(self);
    return jsonify(matchedWorkers);

#GET worker by office
@app.route('/work/office/<office>', methods=["GET"])
def getWorkersByOffice(office):
    self = "office";
    matchedWorkers = [worker for worker in workers if worker.get('office') == office]
    if not matchedWorkers:
        return errorFunc(self);
    return jsonify(matchedWorkers);
    

#GET worker by name
@app.route('/work/name/<name>', methods=["GET"])
def getWorkersByName(name):
    self= "name";
    matchedWorkers = [worker for worker in workers if worker.get('name') == name]
    if not matchedWorkers:
        return errorFunc(self);
    return jsonify(matchedWorkers);
    

#GET worker by id
@app.route('/work/id/<int:id>', methods=["GET"])
def getWorkersById(id):
    for worker in workers:
        if worker.get('id') == id:
           return jsonify(worker);
    return ["Not found. Have sure that you typed the correct id"];

# #PUT => edit a element by id
# @app.route('/work/<int:id>', methods=["PUT"])
# def editById(id):
#     changedWorker = request.get_json()
#     for indice, worker in enumerate(workers):
#         if worker.get('id') == id:
#             workers[indice].update(changedWorker);

def errorFunc(self):
    mensage = [f"Not found. Have sure that you typed the correct {self} and used the route '/work/{self}/<{self}>'"]
    return mensage

app.run(port=5000, host='localhost',debug=True);