from flask import Flask, make_response, jsonify, request
import mysql.connector

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
        }
);
    
    return make_response(jsonify(workers));