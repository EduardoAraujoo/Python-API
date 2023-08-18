from flask import make_response, jsonify

def deleteWorker(id, connection):
    
    cursor = connection.cursor()
    sql = "DELETE FROM worktable WHERE id=%s; "
    cursor.execute(sql, (id,));
    connection.commit();
    cursor.close();

    return make_response(jsonify(f"the worker with id number: {id} was deleted"))

        