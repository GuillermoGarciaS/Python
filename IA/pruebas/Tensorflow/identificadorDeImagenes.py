import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import math


datos, metadatos = tfds.load('fashion_mnist', as_supervised = True, with_info = True)

datos_entrenamiento, datos_prueba = datos['train'], datos['test']

nombres_clases = metadatos.features['label'].names

print(nombres_clases)

def normalizar(imagenes, etiquetas):
    imagenes = tf.cast(imagenes, tf.float32)
    imagenes /= 255
    return imagenes, etiquetas

datos_entrenamiento = datos_entrenamiento.map(normalizar)
datos_prueba = datos_prueba.map(normalizar)

for imagen, etiqueta in datos_entrenamiento.take(1):
    break

imagen = imagen.numpy().reshape((28,28))

plt.figure()
plt.imshow(imagen, cmap = plt.cm.binary)
plt.colorbar()
plt.grid(False)
plt.show()

plt.figure(figsize = (10,10))
for i, (imagen, etiqueta) in enumerate(datos_entrenamiento.take(25)):
    imagen = imagen.numpy().reshape((28,28))
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(imagen, cmap = plt.cm.binary)
    plt.xlabel(nombres_clases[etiqueta])
plt.show()

modelo = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # Flatten layer is here
    tf.keras.layers.Dense(50, activation=tf.nn.relu),
    tf.keras.layers.Dense(50, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax),
])

modelo.compile(
    optimizer = 'adam',
    loss = tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics = ['accuracy']

)

num_ej_entrenamiento = metadatos.splits["train"].num_examples
num_ej_pruebas = metadatos.splits["test"].num_examples

print(num_ej_entrenamiento)
print(num_ej_pruebas)

tamano_lote = 32

datos_entrenamiento = datos_entrenamiento.shuffle(num_ej_entrenamiento).batch(tamano_lote).cache().repeat()
datos_prueba = datos_prueba.batch(tamano_lote).cache().repeat()


historial = modelo.fit(datos_entrenamiento, epochs=5, steps_per_epoch=math.ceil(num_ej_entrenamiento / tamano_lote))

# Retrieve the loss values from the training history
loss_values = historial.history['loss']

plt.plot(loss_values)
plt.xlabel('# Epoch')
plt.ylabel('Loss')
plt.title('Training Loss Over Epochs')
plt.show()

def graficar_imagen(i, arr_predicciones, etiquetas_reales, imagenes):
    arr_predicciones, etiqueta_real, img = arr_predicciones[i], etiquetas_reales[i], imagenes[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img[...,0], cmap = plt.cm.binary)

    etiqueta.prediccion = np.argmax (arr_predicciones)
    if (etiqueta_prediccion == etiqueta_real):
        color = 'blue'
    else:
        color = 'red'

    