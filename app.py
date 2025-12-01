from flask import Flask, send_from_directory, request, jsonify
from clase import Concesionaria, cargar_catalogo

app = Flask(_name_, static_folder=".", static_url_path="")


vehiculos = cargar_catalogo('inventario.txt')
concesionaria = Concesionaria(vehiculos)


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)


@app.route("/ping")
def ping():
    return {"status": "ok"}


@app.route("/api/inventario", methods=["GET"])
def api_listar():
    lista = []
    for v in concesionaria.inventario:
        lista.append({
            "id": v.num_id,
            "tipo": v._class.name_,
            "marca": v.marca,
            "modelo": v.modelo,
            "precio": v.precio
        })
    return jsonify(lista)


@app.route("/api/agregar", methods=["POST"])
def api_agregar():
    data = request.json
    tipo = data.get("tipo")
    
    if tipo == "Bicicleta":
        from clase import Bicicleta
        bici = Bicicleta(
            num_id=concesionaria.generador_id(),
            marca=data.get("marca"),
            modelo=data.get("modelo"),
            color=data.get("color",""),
            anio=int(data.get("anio",2025)),
            tipo_alimentacion=None,
            modalidad=data.get("modalidad","Urbana"),
            tipo_freno=data.get("tipo_freno","Mecanico"),
            precio=float(data.get("precio")),
            rodado=data.get("rodado","26"),
            talle=data.get("talle","M"),
            transmision=data.get("transmision","")
        )
        concesionaria.agregar_vehiculo(bici)
        return jsonify({"status": "ok", "mensaje": "Bicicleta agregada"})
    
    elif tipo == "Auto":
        from clase import Auto
        auto = Auto(
            num_id=concesionaria.generador_id(),
            marca=data.get("marca"),
            modelo=data.get("modelo"),
            color=data.get("color",""),
            anio=int(data.get("anio",2025)),
            tipo_alimentacion=data.get("tipo_alimentacion","Combustion"),
            modalidad=data.get("modalidad","Sedan"),
            tipo_freno=data.get("tipo_freno","Disco"),
            precio=float(data.get("precio")),
            motor=int(data.get("motor",1500)),
            cant_puertas=int(data.get("cant_puertas",4)),
            capacidad_tanque=float(data.get("capacidad_tanque",50))
        )
        concesionaria.agregar_vehiculo(auto)
        return jsonify({"status": "ok", "mensaje": "Auto agregado"})
    
    elif tipo == "Motocicleta":
        from clase import Motocicleta
        moto = Motocicleta(
            num_id=concesionaria.generador_id(),
            marca=data.get("marca"),
            modelo=data.get("modelo"),
            color=data.get("color",""),
            anio=int(data.get("anio",2025)),
            tipo_alimentacion=data.get("tipo_alimentacion","Combustible"),
            modalidad=data.get("modalidad","Urbana"),
            tipo_freno=data.get("tipo_freno","Disco"),
            precio=float(data.get("precio")),
            tamanio_motor=int(data.get("tamanio_motor",150)),
            tipo_motor=data.get("tipo_motor","Monocilindrico"),
            tipo_ciclo=int(data.get("tipo_ciclo",2))
        )
        concesionaria.agregar_vehiculo(moto)
        return jsonify({"status": "ok", "mensaje": "Motocicleta agregada"})
    
    return jsonify({"status":"error","mensaje":"Tipo de vehículo no válido"}),400


@app.route("/api/eliminar/<int:num_id>", methods=["DELETE"])
def api_eliminar(num_id):
    mensaje = concesionaria.eliminar_vehiculo(num_id)
    return jsonify({"mensaje": mensaje})


@app.route("/api/vender/<int:num_id>", methods=["POST"])
def api_vender(num_id):
    mensaje = concesionaria.venta_vehiculo(num_id)
    return jsonify({"mensaje": mensaje})


@app.route("/api/modificar_precio/<int:num_id>", methods=["POST"])
def api_modificar_precio(num_id):
    data = request.json
    nuevo_precio = float(data.get("precio"))
    mensaje = concesionaria.modificar_precio(num_id, nuevo_precio)
    return jsonify({"mensaje": mensaje})

if _name_ == "_main_":
    app.run(debug=True)
