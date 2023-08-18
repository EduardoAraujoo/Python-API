from flask import Flask, make_response, jsonify, request

def getWorkersFunction(cursor):
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
        return workers;

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
    cursor = connection.cursor();
    sql = ('SELECT * FROM worktable WHERE name=%s')
    cursor.execute(sql, (name,));
    workers = getWorkersFunction(cursor);
    cursor.close();
    return make_response(jsonify(workers));

def getWorkersByOffice(office, connection):
    cursor = connection.cursor();
    sql = ('SELECT * FROM worktable WHERE office=%s')
    cursor.execute(sql, (office,));
    workers = getWorkersFunction(cursor);
    cursor.close();
    return make_response(jsonify(workers));