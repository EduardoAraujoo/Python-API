from flask import Flask, make_response, jsonify, request
import difflib

def getWorkersFunction(dados_do_banco):
    similarityResults = list();
    for worker in dados_do_banco:
        similarityResults.append(
        {
            'id' : worker[0],
            'name' : worker[1],
            'office' : worker[2],
            'title' : worker[3]
        });
        
    return similarityResults;

def getWorkers(connection):
    cursor = connection.cursor();
    cursor.execute('SELECT * FROM worktable');
    my_workers = cursor.fetchall();

    workers = list();
    for worker in my_workers:
        workers.append(
        {
            'id' : worker[0],
            'name' : worker[1],
            'office' : worker[2],
            'title' : worker[3]
        });
    return make_response(jsonify(workers));

def getWorkersById(id, connection):
    cursor = connection.cursor();
    sql = ('SELECT * FROM worktable WHERE id=%s')
    cursor.execute(sql, (id,));
    workers = getWorkersFunction(cursor);
    cursor.close();
    return make_response(jsonify(workers));

def getWorkersByTitle(title, connection):
    cursor = connection.cursor();
    sql = ('SELECT * FROM worktable WHERE title=%s')
    cursor.execute(sql, (title,));
    workers = getWorkersFunction(cursor);
    cursor.close();
    return make_response(jsonify(workers));  
    
def getWorkersByName(name, connection):
    cursor = connection.cursor()

    sql = "SELECT * FROM worktable WHERE name LIKE %s"
    cursor.execute(sql, (name + "%",))
    
    dados_do_banco = cursor.fetchall()
    similarityResults = []

    for resultado in dados_do_banco:
        same = difflib.SequenceMatcher(None, name, resultado[1]).ratio()
        if same >= 0.6:
            resultado_com_similaridade = getWorkersFunction(dados_do_banco);
            similarityResults.append(resultado_com_similaridade);

    cursor.close()
    return make_response(jsonify(similarityResults))

def getWorkersByOffice(office, connection):
    cursor = connection.cursor();
    sql = ('SELECT * FROM worktable WHERE office=%s')
    cursor.execute(sql, (office,));
    workers = getWorkersFunction(cursor);
    cursor.close();
    return make_response(jsonify(workers));