import tkinter as tk
from pymongo import MongoClient

def display_data():
    # Conectamos a MongoDB
    client = MongoClient('mongodb://localhost:27017/')

    # Accesamos a la base de datos
    db = client['AgenciaViajes']

    # Accesamos a los datos
    collections = ['Cliente', 'Grupo_Familiar', 'Vuelo']

    for collection_name in collections:
        # Obtenemos la coleccion
        collection = db[collection_name]

        # Hallamos los documentos
        documents = collection.find()

        # Creamos un lable
        label = tk.Label(frame, text=f"Documents in {collection_name} collection:")
        label.pack()

        # Creamos una opccion para poder "scrollear"
        text_widget = tk.Text(frame, height=10, width=60)
        text_widget.pack()

        # Insertamos los documentos
        for document in documents:
            text_widget.insert(tk.END, f"{document}\n\n")

    # Cerramos la conexión
    client.close()

# Creamos la ventana de tk
window = tk.Tk()
window.title("MongoDB Data Display")

# Creamos el frame para crear el widget
frame = tk.Frame(window)
frame.pack(padx=10, pady=10)

# Hacemos un botos para poder generar las tablas
display_button = tk.Button(window, text="Display Data", command=display_data)
display_button.pack()

# Corremos
window.mainloop()


# Trigger

# Conexión a la base de datos
client = MongoClient('localhost', 27017)
db = client['nombre_de_tu_base_de_datos']

# Crear la colección para el trigger con un esquema de validación
db.create_collection(
    "VueloTrigger",
    validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['Numero_vuelo', 'Estado_Vuelo', 'Capacidad_Vuelo'],
            'properties': {
                'Numero_vuelo': {
                    'bsonType': 'string',
                    'description': 'Debe ser una cadena y es obligatorio'
                },
                'Estado_Vuelo': {
                    'bsonType': 'string',
                    'description': 'Debe ser una cadena y es obligatorio'
                },
                'Capacidad_Vuelo': {
                    'bsonType': 'int',
                    'minimum': 0,
                    'maximum': 160,
                    'description': 'Debe ser un entero entre 0 y 160 y es obligatorio'
                }
            }
        }
    },
    validationLevel='moderate',
    validationAction='error'
)

# Insertar un documento de ejemplo en la colección VueloTrigger
db.VueloTrigger.insert_one({
    'Numero_vuelo': 'VL123',
    'Estado_Vuelo': 'Programado',
    'Capacidad_Vuelo': 160
})

# Activar el trigger en la colección Vuelo
with db.Vuelo.watch([
    # Seleccionar solo las operaciones de inserción
    {'$match': {'operationType': 'insert'}},
    # No incluir el _id del documento en el resultado
    {'$project': {'documentKey': False}}
]) as stream:
    for change in stream:
        # Obtener el documento insertado
        vuelo = change['fullDocument']
        # Verificar la capacidad restante del vuelo y actualizar el estado en consecuencia
        if vuelo['Capacidad_Vuelo'] == 0:
            # Si la capacidad es cero, actualizar el estado a "Agotado"
            db.Vuelo.update_one(
                {'_id': vuelo['_id']},
                {'$set': {'Estado_Vuelo': 'Agotado'}}
            )
        elif vuelo['Capacidad_Vuelo'] < 50:
            # Si la capacidad es menor a 50, actualizar el estado a "Casi completo"
            db.Vuelo.update_one(
                {'_id': vuelo['_id']},
                {'$set': {'Estado_Vuelo': 'Casi completo'}}
            )