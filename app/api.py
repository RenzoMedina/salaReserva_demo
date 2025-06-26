from flask import Flask, request, jsonify
from app.reservas import verificarDisponibilidad

app = Flask(__name__)
reservas = []

@app.route("/reservar", methods=['POST'])
def reservar():
    data = request.get_json()
    disponible = verificarDisponibilidad(reservas,data)

    if disponible:
        reservas.append(data)
        return jsonify({"mensaje:":"Reservada con éxito"}), 201
    else:
        return jsonify({"mensaje:":"Sala no disponible"}), 409