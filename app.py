# CRUD
# Create - Read - Update - Delete

from flask import Flask, request
from flask import jsonify
from clubes.clubes_mock import clubes


app = Flask(__name__)


# Devuelve todos los clubes de la base de datos.
@app.route('/clubes')
def get_clubes():
    return jsonify(clubes)


@app.route('/clubes/add', methods=['POST'])
def create_club():
    nuevo_nombre = request.form.get('nombre', '')
    nuevo_fundacion = request.form.get('fundacion', '')

    club = {
        'id': len(clubes)+1,
        'nombre': nuevo_nombre,
        'fundacion': nuevo_fundacion
    }
    clubes.append(club)
    return jsonify(club)


@app.route('/clubes/update/<int:id>', methods=['POST'])
def club_update(id):
    nuevo_nombre = request.form.get('nombre', '')
    nuevo_fundacion = request.form.get('fundacion', '')
    for club in clubes:
        if club.get('id') == id:
            club['nombre'] = nuevo_nombre or club.get('nombre')
            club['fundacion'] = nuevo_fundacion or club.get('fundacion')
            return jsonify(club)
    return 'Peticion mal realizada. Numero de id incorrecto', 401


@app.route('/clubes/delete/<int:id>', methods=['DELETE'])
def delete_club(id):
    for club in clubes:
        if club.get('id') == id:
            clubes.remove(club)
            return '', 200
    return '', 401

if __name__ == '__main__':
    app.run(port=3000, debug=True)
