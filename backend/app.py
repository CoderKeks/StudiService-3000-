from flask import Flask, jsonify, request
from flask_cors import CORS

from Service.StudierendeService import StudierendeService
from Models.Studierender import Studierender

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

studierende_service = StudierendeService()

@app.route('/api/studierende', methods=['GET'])
def get_all_studierende():
    studierende = studierende_service.get_all()
    return jsonify([s.to_dict() for s in studierende])

@app.route('/api/studierende/<int:studierende_id>', methods=['GET'])
def get_studierende(studierende_id):
    s = studierende_service.get_one(studierende_id)
    if s:
        return jsonify(s.to_dict())
    return jsonify({"error": "Not found"}), 404

@app.route('/api/studierende', methods=['POST'])
def create_studierende():
    data = request.get_json()
    s = Studierender(
        name=data['name'],
        matrikelnummer=data['matrikelnummer'],
        studiengang=data['studiengang']
    )
    new_id = studierende_service.create(s)
    return jsonify({"id": new_id})

@app.route('/api/studierende/<int:studierende_id>', methods=['PUT'])
def update_studierende(studierende_id):
    data = request.get_json()
    s = Studierender(
        name=data['name'],
        matrikelnummer=data['matrikelnummer'],
        studiengang=data['studiengang']
    )
    updated = studierende_service.update(studierende_id, s)
    return jsonify({"updated": updated})

@app.route('/api/studierende/<int:studierende_id>', methods=['DELETE'])
def delete_studierende(studierende_id):
    deleted = studierende_service.delete(studierende_id)
    return jsonify({"deleted": deleted})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 
