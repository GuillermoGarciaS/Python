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
