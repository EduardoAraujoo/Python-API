from flask import Flask, make_response, jsonify, request

def deleteWorker(id, connection):
    
    cursor = connection.cursor()
    sql = "DELETE FROM worktable WHERE id=%s; "
    cursor.execute(sql, (id,));
    connection.commit();
    cursor.close();

    return make_response(jsonify(f"the worker with id number: {id} was deleted"))
    # for indice, worker in enumerate(workers):
    #     if worker.get('id') == id:
    #         del workers[indice]
        