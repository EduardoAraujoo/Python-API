from flask import make_response, jsonify, request

def editById(id, connection):
    changedWorker = request.get_json()
    
    cursor = connection.cursor()
    sql = "UPDATE worktable SET name=%s, office=%s, title=%s WHERE id=%s"
    cursor.execute(sql, (changedWorker['name'], changedWorker['office'], changedWorker['title'], id))
    connection.commit();
    cursor.close();
       
    return make_response(jsonify(changedWorker))
