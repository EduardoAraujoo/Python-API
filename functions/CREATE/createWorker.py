from flask import Flask, make_response, jsonify, request

def createWorker(connection):
    newWorker = request.get_json();
    # workers.append(newWorker);
    
    cursor = connection.cursor();
    sql = f'INSERT INTO worktable (name, office, title) VALUES ("{newWorker["name"]}", "{newWorker["office"]}", "{newWorker["title"]}")'
    cursor.execute(sql);
    connection.commit();

    return make_response(
        jsonify(newWorker)
        );